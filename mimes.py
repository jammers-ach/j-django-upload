

import magic
from django.conf import settings
media_root = getattr(settings, "MEDIA_ROOT", "media")
import os

def get_mime(filename):
    '''gets the mimetype for a file, with some thing not too specific'''
    try:
        return magic.from_file(os.path.join(media_root,filename) ,mime=True).replace('/','-')
    except IOError,e:
        return 'default'


