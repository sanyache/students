function initJournal(){
    var indicator = $('#ajax-progress-indicator');
    $('.day-box input[type="checkbox"]').click(function(event){
        var box = $(this);
        $.ajax(box.data('url'),{
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data':{
            'pk': box.data('student-id'),
            'date': box.data('date'),
            'present': box.is(':checked')? '1': '',
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
        },
        'beforeSend': function(xhr, settings){
            indicator.show();

        },
        'error': function(xhr, status, error){
            alert(error);
            indicator.hide();
        },
        'success': function(data, status, xhr){
            indicator.hide();
        }
        });
    });
}

function initGroupSelector(){
    $('#group-selector select').change(function(event){
        var group = $(this).val();
        if (group){
            $.cookie('current_group', group, {'path': '/', 'expires': 365});
        }else{
            $.removeCookie('current_group', {'path': '/'});
        }
        location.reload(true);
        return true;
    });
}

function initDateFields(){
    $('input.dateinput').datetimepicker({
        'format': 'YYYY-MM-DD'
    }).on('dp.hide', function(event){
        $(this).blur();
    });
}

function initEditStudentPage(){
    $('a.student-edit-form-link').click(function(event){
        var link = $(this);
                $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'success': function(data, status, xhr){
                if (status != 'success'){
                    alert('Помилка на сервері. Спробуйте пізніше.');
                    return false;
                }
                var modal = $('#myModal'), html = $(data), form = html.find('#content-column form');
                modal.find('.modal-title').html(html.find('#content-column h2').text());
                //modal.find('.modal-body').html(form);
                var modalImg = document.getElementById('img00'), divimg = html.find('#div_id_photo a').attr('href');
                linkImg = "http://127.0.0.1:8000"+ divimg;
                modalImg.src = linkImg;
                modal.find('.modal-body').html(form);
                initEditStudentForm(form, modal);
                modal.modal({
                    'keyboard': false,
                    'backdrop': false,
                    'show': true
                });
                

            },
            'error': function(){
                alert('Помилка на сервері');
                return false;
            }
        });
        return false;
    });
}
function initEditStudentForm(form, modal){

    form.find('input[name="cancel_button"]').click(function(event){
        modal.modal('hide');
        return false;
    });
    form.ajaxForm({
        'dataType': 'html',
        'error': function(){
            alert('Помилка на сервері. Спробуйте пізніше');
            return false;
        },
        
        'success': function(data, status, xhr){
                var html = $(data), newform = html.find('#content-column form');
                modal.find('.modal-body').html(html.find('.alert'));
                if (newform.length>1){
                modal.find('.modal-body').append(newform);
                initEditStudentForm(newform, modal);
                } else {
                  setTimeout(function(){location.reload(true);},500);
              }
            }  
        }); 
}

function initAddStudentPage(){
    $('a.student-add-form-link').click(function(event){
        var link = $(this);
        $.ajax({ 
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'success': function(data, status, xhr){ 
                if (status != 'success'){
                    alert('Помилка на сервері. Спробуйте пізніше.');
                    return false;
                }
                var modal = $('#myModal'), html = $(data), form = html.find('#content-column form');
                modal.find('.modal-title').html(html.find('#content-column h2').text());
                var modalImg = document.getElementById('img00');
                linkImg = "http://127.0.0.1:8000/media/default.jpg";
                modalImg.src = linkImg;
                modal.find('.modal-body').html(form);
                modal.modal('show');
                $('#photo').change(function(){
                    var modalImg = document.getElementById('img00'), divimg=this.value;
                    linkImg = divimg.replace("C:\\fakepath\\", "");
                    modalImg.src = "http://127.0.0.1:8000/media/"+ linkImg;
                });    
                
                

            },
            'error': function(){
                alert('Помилка на сервері');
                return false;
            }
        });
        return false;
    });
}
function initImgPage(){
    var modal = $('#myModal');
    var img = document.getElementsByClassName('img-circle');
    //var lastName = document.getElementsByClassName('last-name');
    var modalImg = document.getElementById("img00");
    var captionText = document.getElementById('caption');
    for(var i=0; i<img.length; i++){
    img[i].onclick = function(){
        modalImg.src = this.src;
        
        captionText.innerHTML = this.alt;
        modal.modal('show');
        return false;}
    }
 }

function initAnimation(){
    $('a.animated').hover(
        function(){
            $(this).addClass('flash');
        },
        function(){
            $(this).removeClass('flash');
        }
    );
}

function initLangSelector(){
    $('#lang-selector select').change(function(event){
        var lang = $(this).val();
        if (lang){
            $.cookie('django_language',lang, {'path': '/'});
        } else {
            $.removeCookie('django_language', {'path': '/'});
        }
        location.reload(true);
        return true;
    });
}
function loadMore(){ 
    var page = 1;
    $('a.load-more').click(function(event){ 
        var link;
        var num_pages = $(this).data('pages');
        page += 1;
        if( page <= num_pages){
            link =  "http://127.0.0.1:8000/?page="+ page;
        
            $.ajax({
                'url': link,
                'dataType': 'html',
                'type': 'get',
                'success': function(data, status, xhr){ 
                    html = $(data).find('tbody');
                    $('table').append(html);
                
                }
            });
        } 
        if( page == num_pages ){
            $(this).hide();
        }
        return false;
    });
}


$(document).ready(function(){ loadMore();
    initJournal();
    initGroupSelector();
    initDateFields();
    initEditStudentPage();
    initAddStudentPage();
    initImgPage();
    initAnimation();
    initLangSelector();
    search();
    
});