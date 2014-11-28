'''
fields.py - contains feilds for handling uploads
'''

from django.db.models import Field,SubfieldBase
from .widgets import MultipleFileWidget

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
