import re
import string
import os
import sys


from tools import killableprocess

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

    def exec_fortran(self, bin):

        stout_tmp = open(os.path.join(self.path_temp, 'stout'), 'w')

        if bin in BIN_AVAILABLE:
            args = []
            if sys.platform != 'win32':
                #On any non-Windows system, we run binaries over wine
                args.append('wine')

            args.append( os.path.join(PATH_BIN, bin + '.exe'))

            ret = killableprocess.call(args, cwd=self.path_temp, stdout=stout_tmp, timeout=TIMEOUT)    #kill if not return in TIMEOUT seconds

            pub.sendMessage('log', ('info', '%s executed' % bin))

            stout_tmp.close()
            
            with open(os.path.join(self.path_temp, 'stout'), 'r') as stout_tmp:
                outputs = stout_tmp.readlines()
                for line in [line.strip() for line in outputs]:
                    pub.sendMessage('log', ('info', "%s output: %s" % (bin, line) ))
                    # print '---%s---' % line
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
            
            curves = []
            token_keys = tokens.keys()
            token_keys.sort()

            for (begin, end) in token_keys:
                #print (begin,end)
                fh.seek(0)

                temp_file_path = os.path.join(self.path_temp, 'temp_gpecout.dat')            #TODO rethink this!
                with open(temp_file_path, 'w') as fho:
                    #write lines just of the block between (begin,end)
                    
                    
                    for l,line in enumerate(fh):
                        if begin <= l < end:
                            #sometimes there are "*" chars which must be removed
                            fho.write( line.replace('*', '') )        
                    fho.close()
                
                #retrieve significative columns from a dictionary. (begin,end)=>type=>num_cols 
                significatives_cols= range(curve_types[tokens[(begin, end)]])     

                curve = np.loadtxt(temp_file_path, usecols=significatives_cols)
                curves.append(curve)

            fh.close()

        pub.sendMessage('add_txt', (filepath, self.case_id))
        return curves
