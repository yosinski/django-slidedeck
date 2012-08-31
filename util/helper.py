# Helper classes / functions

import subprocess
import string
import random



randChars  = '%s%s' % (string.ascii_letters, string.digits)



def randomString(length = 10):
    return ''.join(random.choice(randChars) for ii in xrange(length))



class DuckStruct(object):
    '''Use to store anything!'''
    
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        rep = ['%s=%s' % (k, repr(v)) for k,v in self.__dict__.items()]
        return 'DuckStruct(%s)' % ', '.join(rep)



def runCmd(args, verbose = False):
    if verbose:
        proc = subprocess.Popen(args)
    else:
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,err = proc.communicate()
    code = proc.wait()

    if code != 0:
        print out
        print err
        raise Exception('Got error from running command with args ' + repr(args))

    return out, err
