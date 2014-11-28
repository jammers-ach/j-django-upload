'''
Widgets for ajax file uploading
'''
from django.forms import widgets
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
import os
from mimes import get_mime
class MultipleFileWidget(widgets.Input):


    def __init__(self,*args,**kwargs) :
        super(MultipleFileWidget,self).__init__(*args,**kwargs)
        #
    def render(self, name, value, attrs=None):

        #TODO move this to the init function
        self.target_url = reverse('juploader:default_upload')


        attrs['type'] = 'hidden'
        s = super(MultipleFileWidget,self).render(name,value,attrs)
        text = '<div class="multifile_upload" >'
        text += '<div class="file_uploader" data-url="%s"></div>' % self.target_url
        text += s
        text += '<div class="current_files">%s</div>' % self.make_icons(value)
        text += '</div>'
        return mark_safe(text)


    def make_icons(self,value):
        '''from this objects comma seperated list of files it makes little icons matching their mimetype'''
        text = ''
        if(value != None):
            for fname in value.split(','):
                if(fname != ''):
                    mimetype = get_mime(fname)
                    filename = os.path.split(fname)[-1]
                    text += '<div class="file"><div class="ficon %s"></div><span>%s</span> <a target="_blank" href="/media/%s"><span></span></a></span></div>' % (mimetype,filename,fname)

        return text

    class Media:
        css = {
            'all': ('jdjango_upload/css/jdjango_upload.css','jdjango_upload/css/mimetypes.css','ajaxuploader/css/fileuploader.css')
        }
        js = ('jdjango_upload/js/uploader.js',
              'ajaxuploader/js/fileuploader.js',) #TODO find out how to reference jquery properly)

