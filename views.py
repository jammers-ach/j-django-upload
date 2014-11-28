from django.shortcuts import render
from ajaxuploader.views import AjaxFileUploader
from ajaxuploader.signals import file_uploaded
from ajaxuploader.backends.local import LocalUploadBackend
from django.conf import settings
import os
from mimes import get_mime
# Create your views here.

class JUploaderbackend(LocalUploadBackend):

    def __init__(self,*args,**kwargs):
        if('target_dir' not in kwargs):
            self.target_dir = getattr(settings, "DEFAULT_JUPLOAD_DIR", "unsorted_files")
        else:
            self.target_dir = kwargs.pop('target_dir')

        super(JUploaderbackend,self).__init__()
        self.UPLOAD_DIR = os.path.join(self.UPLOAD_DIR,self.target_dir)

    def update_filename(self,request,filename):
        '''filename gets put into the users avatar directory'''
        #TODO detect duplicate files
        filename = filename.replace(',','') #Pesky comas, hate them
        return filename

    def upload_complete(self,request,filename):
        '''resizes the image and converts to PNG'''
        fpath = os.path.join(self.UPLOAD_DIR,filename)
        mimetype = get_mime(fpath)

        return {'mimetype':mimetype,
                'path':fpath,}


uploader_conf = AjaxFileUploader(backend=JUploaderbackend)
