import re
import string
import subprocess
import os
import sys

from settings import PATH_BIN, PATH_TEMP


def exec_fortran(bin):
    #if bin == 'ModelsParam':
    #elif bin == 'PCSAFTparam':
    #elif bin == 'GPEC':
    #elif bin =='PxyGPEC':
    #elif bin == 'TxyGPEC':
    #elif bin == 'IsoplethGPEC':
    #elif bin == 'FUGi':
    #elif bin == 'IsoXT':
    #elif bin == 'PhPxy':
    #elif bin == 'PhTxy':

    args = []
    if sys.platform != 'win32':
        #On any non-Windows system, we run binaries over wine
        args.append('wine')
    args.append( os.path.join(PATH_BIN, bin + '.exe'))

    #fortran binaries need to be called from temporary input files are
    return subprocess.call(args, cwd=PATH_TEMP)



def get_numbers(data_raw, prefix=None):
    """recibes any string and return a list of founded numbers as strings"""

    re_float = re.compile("""[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?""")
    numbers = re.findall(re_float, data_raw)
    if prefix:
        numbers = [n for n in numbers if n.startswith(prefix)]
    return map(string.strip, numbers)



def write_conparin(sense, model, data):
    """Write the input file CONPARIN.DAT ". data could be EOS variables or 
        model paramater""" 

    filename = 'CONPARIN.DAT'
    fh = open( os.path.join(PATH_TEMP, filename), 'w')
    template = "{0}  {1}\n {2}"
    output = template.format (sense, model, "  ".join( data )) 
    fh.write(output)
    fh.close()


def write_gpecin(model, comp1, comp2, ncomb=0, ntdep=0, k12=0.0, l12=0.0, max_p=2000):
    """
    compX -> ('NAME', (const1, ..., constN), (param1, ... , paramM))
    """

    filename = 'GPECIN.DAT'
    fh = open(os.path.join(PATH_TEMP, filename), 'w')
    template = "{0}\n{1} {2}\n%s" % "".join(['{%d}\n' % i for i in range(3, 12)])

    output = template.format(model, ncomb, ntdep, comp1[0], "  ".join(map(str, comp1[1])), 
                            "  ".join(map(str, comp1[2])), comp2[0], "  ".join(map(str, comp2[1])), 
                            "  ".join(map(str, comp2[2])), k12, l12, max_p)
    print output
    fh.write(output)
    fh.close()

def read_conparout():
    """COMPAROUT.DAT has two lines of data. First one is EOS vars and second 
        model parameters. """

    ret = exec_fortran('ModelsParam')
    print ret
    if ret == 0:
        filename = 'CONPAROUT.DAT'
        fh = open(os.path.join(PATH_TEMP, filename), 'r')
        output = [get_numbers(line) for line in fh.readlines()]
        fh.close()
        return output
                
        



    

