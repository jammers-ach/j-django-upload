'''
fields.py - contains feilds for handling uploads
'''

from django.db.models import Field,SubfieldBase
from .widgets import MultipleFileWidget
import os
from django.conf import settings

class MultipleFileField(Field):
    '''A field that contains muliple files uploaded by ajax'''

    description = 'Multiple files, uploaded via ajax'

    __metaclass__ = SubfieldBase

    def __init__(self, *args, **kwargs):
        self.widget = MultipleFileWidget()
        super(MultipleFileField,self).__init__(*args,**kwargs)


    def formfield(self, **kwargs):
        defaults = {'widget': self.widget}
        #defaults = {}
        defaults.update(kwargs)
        return super(MultipleFileField, self).formfield(**defaults)

    def get_internal_type(self):
        return "TextField"


    def move_files(self,new_dir):
        '''Goes through all the files and moves them to the new directory'''
        pass


unsorted_dir = getattr(settings, "DEFAULT_JUPLOAD_DIR", "unsorted_files")

def move_files(obj,field,new_dir):
    '''I would like to do this:
        (in the modles save)
        super(Model,self).save(....)
        self.files1.move_files('%d/new' % self.id)
        self.files2.move_files('%d/incoming' % self.id)
        so that files get moved from 'unsorted_files'
        however I can't create a function in the field class and call it.
        So I've got this guy here

        move_files(self,'files1','%d/new' % self.id)
        '''

    files = getattr(obj,field)

    test_dir = os.path.join('uploads',new_dir)
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    #now go through all the files
    new_files = []
    modified = False
    for i in files.split(','):
        if(i != ''):
            words = i.split('/')
            if(words[1] == unsorted_dir):
                #move the file

                words[1] = new_dir
                new_path = '/'.join(words)

                if(os.path.exists(i)):
                    #we should have the new path here
                    os.rename(i,new_path)
                elif(not os.path.exists(new_path)):
                    raise IOError("Couldn't find old path or new path %s %s" % (i,new_path))

                modified = True
                i = new_path
            new_files.append(i)


    if(modified):
        print 'modified',new_files
        setattr(obj,field,','.join(new_files))
        obj.save()
        print obj.files
