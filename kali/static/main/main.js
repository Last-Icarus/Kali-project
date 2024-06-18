function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

$( document ).ready(function() {
    $('.section p').on('click', function() {
        sibling = $(this).siblings('.section-list')
        if (sibling.css('display') === 'none') {
            $(this).siblings('.section-list').show()
        } else {
            $(this).siblings('.section-list').hide()
        }
    })

    $('.settings_btn').on('click', function() {
        $('#profile_settings').show()
        $('#dimmer').show()
        })
    
    $('.settings_close_btn').on('click', function() {
        console.log('settings close')
        $('#profile_settings').hide()
        $('#dimmer').hide()
        
    })

    $("#profile_form").submit(function(e) {
        e.preventDefault();
        dataform = $('#profile_form').serialize()
        $.post('/save_settings/', dataform, function(data) {
            console.log(data)
        })
    });

    $('.notification').show()

    $('.studio_menu input').change(function() {
        n = $(this).attr('id').slice(-1)
        $('.studio_content > div').hide()
        $('.studio_content > div:nth-child(' + n + ')').show()
    })

    $('#add_img_btn').click(function() {
        n = $('.images_list input:visible').length
        $('#id_form-' + n + '-image').show()
        if (n>4) {
            $('#add_img_btn').hide()
        }
    })

    $('#create_art_btn').click(function() {
        dataform = $('#art_info_form').serialize() + '&' + $('#create_art_form').serialize() 
        $.post('/create-art/', dataform, function(data) {
            console.log(data)
        })
    })
});

