            // preload gif
          $(window).load(function() {
        $('#status').fadeOut();
        $('#preloader').delay(300).fadeOut('slow');
      });
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
   
      
      $('.owl-carousel').owlCarousel({
        animateOut: 'slideOutDown',
          animateIn: 'flipInX',
          items:2,
          loop:true,
          margin:10,
           nav:true,
          responsiveClass:true,
      })
          // Carousel items detials
      jQuery(document).ready(function($) {

        $('#myCarousel').carousel({
                interval: 5000
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
      });  