      $(function(){ 
            function itemActive($el) {
                $el.siblings().removeClass('active');
                $el.addClass('active');
            }
            var settings = {
                slideMargin: 1,
                minSlides: 3,
                maxSlides: 4,
                slideWidth: false,
                infiniteLoop: false,
                responsive: true,
                controls: true,
                pager: false,
                moveSlides: 1,
                hideControlOnEnd: true,
                onSlideNext: function($slideElement, oldIndex, newIndex) {
                  itemActive($slideElement);
                },
                onSlidePrev: function($slideElement, oldIndex, newIndex) {
                  itemActive($slideElement);
                }
            }

            var bxSlider = $('.productslider').bxSlider(settings);

            $('.productslider li').click(function(){
                $(this).siblings('li').removeClass('active');
                $(this).addClass('active');
                bxSlider.goToSlide($(this).index());
                
            });
        });

        $(function(){ 
            function itemActive($el) {
                $el.siblings().removeClass('active');
                $el.addClass('active');
            }
            var settings = {
                slideMargin: 2,
                minSlides: 3,
                maxSlides: 40,
                slideWidth: 150,
                infiniteLoop: false,
                responsive: true,
                controls: true,
                pager: false,
                moveSlides: 1,
                hideControlOnEnd: true,
                onSlideNext: function($slideElement, oldIndex, newIndex) {
                  itemActive($slideElement);
                },
                onSlidePrev: function($slideElement, oldIndex, newIndex) {
                  itemActive($slideElement);
                }
            }

            var bxSlider = $('.partnerslider').bxSlider(settings);
        
        });

        $(function(){ 
            function itemActive($el) {
                $el.siblings().removeClass('active');
                $el.addClass('active');
            }
            var settings = {
                slideMargin: 1,
                minSlides: 1,
                maxSlides: 40,
                infiniteLoop: false,
                responsive: true,
                controls: true,
                pager: true,
                moveSlides: 1,
                hideControlOnEnd: true,
                onSlideNext: function($slideElement, oldIndex, newIndex) {
                  itemActive($slideElement);
                },
                onSlidePrev: function($slideElement, oldIndex, newIndex) {
                  itemActive($slideElement);
                }
            }

            var bxSlider = $('.sayslider').bxSlider(settings);
        
        });