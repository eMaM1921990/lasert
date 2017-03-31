/**
 * Created by mac on 3/24/17.
 */
function changeAppLanguage(langCode){
    $.ajax({
        url: "/i18n/setlang/",
        type: 'POST',
        data:{
            language:langCode,
            next:'/',
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        success: function (responseText) {
               window.location.reload();
        },
        error: function (xhr, errmsg, err) {
            console.log(errmsg);
        }
    });
}


function subscripe(){
    var df = new FormData(document.getElementById('subscribe_form'));
    $.ajax({
        url: "/subscribe/",
        type: 'POST',
        cache: false,
        contentType: false,
        processData: false,
        data: df,
        success: function (responseText) {
               console.log(responseText);
                $('#email').val('');
        },
        error: function (xhr, errmsg, err) {
            console.log(errmsg);
        }
    });
}