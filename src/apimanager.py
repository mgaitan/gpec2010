import re
import string
import os
import sys

import cStringIO #for memory files


from tools import killableprocess
import subprocess

from settings import PATH_BIN, TIMEOUT, PATH_TEMP, BIN_AVAILABLE
import numpy as np

from wx.lib.pubsub import Publisher as pub


def clean_tmp():
    """auxiliary function to clean all temporary files/dirs"""
    def rm_content(path):
        for the_file in os.listdir(path):
            file_path = os.path.join(path, the_file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path) and os.path.split(file_path)[1] != '.svn' :
                    rm_content(file_path)   #recursiveness
            except Exception, e:
                print e
        if path != PATH_TEMP:
            os.rmdir(path)

    rm_content(PATH_TEMP)


def get_numbers(data_raw, prefix=None):
    """recibes any string and return a list of numbers found as strings"""

    re_float = re.compile("""[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?""")
    numbers = re.findall(re_float, data_raw)
    if prefix:
        numbers = [n for n in numbers if n.startswith(prefix)]
    return map(string.strip, numbers)




class ApiManager():
    def __init__(self, case_id):
        self.case_id = case_id
        os.mkdir(os.path.join(PATH_TEMP, str(self.case_id)))    #make a temporary directory exclusive
        self.path_temp = os.path.join(PATH_TEMP, str(self.case_id))
        
        self.written = {}   #flags

    def exec_fortran(self, bin):


        if bin in BIN_AVAILABLE.keys():
            args = []
            if sys.platform != 'win32':
                #On any non-Windows system, we run binaries through wine
                args.append('wine')

            args.append( os.path.join(PATH_BIN, bin + '.exe'))

            proc = killableprocess.Popen(args, cwd=self.path_temp, stdout=subprocess.PIPE)    #kill if not return in TIMEOUT seconds
            ret = proc.wait(timeout=TIMEOUT)

            pub.sendMessage('log', ('ok', '%s executed' % bin))

            for line  in proc.communicate()[0].splitlines():        #read stdout and send to log panel
                if line.strip():
                    pub.sendMessage('log', ('info', "%s output: %s" % (bin, line) ))
                
            return ret
        else:
            pub.sendMessage('log', ('error', 'Unknown fortran executable %s' % bin))

    def write_conparin(self, direction, model_id, data):
        """Write the input file CONPARIN.DAT ". data could be EOS variables or 
            model paramater""" 

        filename = 'CONPARIN.DAT'
        filepath = os.path.join(self.path_temp, filename)
        template = "{0}  {1}\n {2}"


        if model_id in (1,2,3):
            data = data[:-2] + [data[-1], data[-2]]
        elif model_id in (4,6):
            data = data[:-2] + [data[-1]]


        output = template.format (direction, model_id, "  ".join( data )) 
        with open(filepath , 'w') as fh:
            fh.write(output)
            fh.close()
    
    
        self.written[filename] = True
        pub.sendMessage('add_txt', (filepath, self.case_id))

    def write_gpecin(self, model, comp1, comp2, ncomb=0, ntdep=0, k12=0.0, l12=0.0, max_p=2000):
        """
        compX -> ('NAME', (const1, ..., constN), (param1, ... , paramM))
        """

        filename = 'GPECIN.DAT'
        filepath = os.path.join(self.path_temp, filename)
        template = "{0}\n{1} {2}\n%s" % "".join(['{%d}\n' % i for i in range(3, 12)])

        if model == 4:                  #TODO  - this shoul come solved from the form, keeping a copy af acentric_factor
            comp1[1].append('1.168')
            comp2[1].append('1.168')

        output = template.format(model, ncomb, ntdep, comp1[0], "  ".join(map(str, comp1[1])), 
                                "  ".join(map(str, comp1[2])), comp2[0], "  ".join(map(str, comp2[1])), 
                                "  ".join(map(str, comp2[2])), k12, l12, max_p)
        
        with open(filepath, 'w') as fh:     #writing in path_bin instead self.path_temp
            fh.write(output)
            fh.close()

        self.written[filename] = True
        pub.sendMessage('add_txt', (filepath, self.case_id))


    def read_conparout(self, model_id):
        """COMPAROUT.DAT has two lines of data. First one is EOS vars and second 
            model parameters. """

        if model_id in (4,6):
            ret = self.exec_fortran('PCSAFT')
        else:
            ret = self.exec_fortran('ModelsParam')

        if ret == 0:
            filename = 'CONPAROUT.DAT'
            filepath = os.path.join(self.path_temp, filename)
            with open(filepath, 'r') as fh:
                output = [get_numbers(line) for line in fh.readlines()]
                
            pub.sendMessage('add_txt', (filepath, self.case_id))

            return output
                    
            
    def read_gpecout(self):
        """Parses an gpecout.dat, detects numeric blocks and create arrays with them"""

        ret = self.exec_fortran('GPEC')  #generate gpecout.dat
        
        
        
        filename = 'GPECOUT.DAT'

        filepath = os.path.join(self.path_temp, filename)
        curve_types = {'VAP':4, 'CRI':5, 'CEP':6, 'LLV':10 } #type:significatives columns

        tokens = {}         #{(begin,end):'type', ...}
        begin = end = 0
        
        with open(filepath, 'r') as fh:
           

            number_of_lines = len(fh.readlines())
            fh.seek(0)
            
            #give skip from header and skip from footer
            for line_number, line in enumerate(fh):
                if begin <= end:
                    #looking for a curve TOKEN : 'VAP', 'CRI' etc...
                    if line.strip() in curve_types:
                        begin = line_number + 1
                        curve_type = line.strip()
                else:
                    #looking for a blank line which determines the end of arrays block.
                    if not line.strip():
                        end = line_number
                        tokens[(begin, end)] = curve_type
            
            arrays_out = {}     #Format: {type: [array1, array2, ... ], ...  }
            
            
            for (begin, end), curve_type in sorted(tokens.items()):
                

                fh.seek(0)
                
                temp_w = cStringIO.StringIO()       #a memory file to write 
                
                #write lines just of the block between (begin,end)
                for l,line in enumerate(fh):
                    if begin <= l < end:
                        temp_w.write( line )    
            

                temp_r = cStringIO.StringIO(temp_w.getvalue())      #and copy to read
                

                #retrieve significative columns from a dictionary. (begin,end)=>type=>num_cols 
                significatives_cols= range(curve_types[tokens[(begin, end)]])

                curve_array = np.loadtxt(temp_r, usecols=significatives_cols)

                temp_w.close()
                temp_r.close()


                #if it's a new type on the dict, create it.
                if curve_type not in arrays_out.keys():
                    arrays_out[curve_type] = []         #TODO should it be a ndarray ?
                
                arrays_out[curve_type].append(curve_array)


            fh.close()

        pub.sendMessage('add_txt', (filepath, self.case_id))
        return arrays_out
