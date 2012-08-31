# Helper classes / functions



class DuckStruct(object):
    '''Use to store anything!'''
    
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        rep = ['%s=%s' % (k, repr(v)) for k,v in self.__dict__.items()]
        return 'DuckStruct(%s)' % ', '.join(rep)
