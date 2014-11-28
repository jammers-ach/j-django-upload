// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function make_icon(jsonData,fname){
    text ="<div class='file'>"
    text += '<div class="ficon "'+jsonData['mimetype'] +'"/>'
    text += '<span>' +fname+ '</span>'
    text += '<a target="_blank" href="/media/'+jsonData['path']+ '"/><span></span></a></span>'
    text += '</div>'
    return text
}

$(function(){
    var csrftoken = getCookie('csrftoken');

    console.log(csrftoken);

    $('.file_uploader').each(function(){
        var us = this;
        var our_input = $(this).parent().find('input');
        var our_filepath = $(this).parent().find('.current_files');
        url = this.getAttribute('data-url');

        new qq.FileUploader({
            element:us,
            multiple:true,
            action:url,

            onComplete:function(id,filename,responseJSON){
                if(!responseJSON.success){
                    alert('upload failed!');
                }
                console.log(responseJSON);

                our_input.val( our_input.val() + ',' + responseJSON['path']);
                our_filepath.append(make_icon(responseJSON,filename));
            },params: {
              'csrf_token':csrftoken,
              'csrf_name': 'csrfmiddlewaretoken',
              'csrf_xname': 'X-CSRFToken',
            },
        });
    })
});
