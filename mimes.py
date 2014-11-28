

import magic

def get_mime(filename):
    '''gets the mimetype for a file, with some thing not too specific'''
    try:
        return magic.from_file(filename,mime=True).replace('/','-')
    except IOError,e:
        return 'default'


