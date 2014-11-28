

import magic

def get_mime(filename):
    return magic.from_file(filename,mime=True).replace('/','-')


