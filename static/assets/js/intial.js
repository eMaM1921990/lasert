 
      // end preload gif
      $(window).scroll(function() {
        if ($(document).scrollTop() > 200) {
          $('nav').addClass('shrink');
          $('.top-menu').addClass('hidden');
        } else {
          $('nav').removeClass('shrink');
          $('.top-menu').removeClass('hidden');
        }
      });
   
      

        $(window).load(function () {
            // Animate loader off screen
            $(".se-pre-con").fadeOut("slow");
            ;
        });
        


        //Handles the carousel thumbnails
        $('[id^=carousel-selector-]').click(function () {
        var id_selector = $(this).attr("id");
        try {
            var id = /-(\d+)$/.exec(id_selector)[1];
            console.log(id_selector, id);
            jQuery('#myCarousel').carousel(parseInt(id));
        } catch (e) {
            console.log('Regex failed!', e);
        }
        });
        // When the carousel slides, auto update the text
        $('#myCarousel').on('slid.bs.carousel', function (e) {
                 var id = $('.item.active').data('slide-number');
                $('#carousel-text').html($('#slide-content-'+id).html());
        });
     