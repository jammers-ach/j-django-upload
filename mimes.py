

import magic

def get_mime(filename):
    '''gets the mimetype for a file, with some thing not too specific'''
    return magic.from_file(filename,mime=True).replace('/','-')


