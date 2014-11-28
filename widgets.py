'''
Widgets for ajax file uploading
'''
from django.forms import widgets
from django.utils.safestring import mark_safe

class MultipleFileWidget(widgets.Input):


    def __init__(self,*args,**kwargs) :
        super(MultipleFileWidget,self).__init__(*args,**kwargs)

    def render(self, name, value, attrs=None):
        attrs['type'] = 'hidden'
        s = super(MultipleFileWidget,self).render(name,value,attrs)
        text = '<div class="multifile_upload">'
        text += value
        text += s
        text += '</div>'
        return mark_safe(text)
