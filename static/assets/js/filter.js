        $(".filterMenu").find('button').on('click', function(){
 
  $(".filterMenu").find('button').removeClass('btn-danger');
  $(".filterMenu").find('button').addClass('btn-default');
    
  $(this).addClass('btn-danger');
  
});

$(".sorteerMenu").find('button').on('click', function(){
 
  $(".sorteerMenu").find('button').removeClass('btn-danger');
  $(".sorteerMenu").find('button').addClass('btn-default');
    
  $(this).addClass('btn-danger');
  
});

$('.keuze').find('label').on('click', function(){
  $('.keuze').find('label').removeClass('active');
  $(this).addClass('active');
  search();
});

function search(){
 
    var $grid = $('.grid').isotope ({
    itemSelector: '.grid-item',
    //layoutMode: 'fitRows',
    getSortData: {
        geslacht: '.geslacht',
        views: '.views parseInt',
        aantal: '.aantal parseInt'
      },
    sortAscending: {
        geslacht: false,
        views: false,
        aantal: true
      }
});
  
  // filter items on button click
    $('.filterMenu').find('button').on( 'click', function() {
      var filterValue = $(this).attr('data-filter');
      $grid.isotope({ filter: filterValue });
    });
  
   // sort items on button click
    $('.sorteerMenu').find('button').on( 'click', function() {
      var sortByValue = $(this).attr('data-sort-by');
      $grid.isotope({ sortBy: sortByValue });
});
  
  var option = $('.active').find('input').attr('id');
  
  if(option == "option1"){ //filter
    $('.filterMenu').removeClass('hidden');
    $('.sorteerMenu').addClass('hidden');
    
  } else if(option =="option2"){ //sorteer
    $('.filterMenu').addClass('hidden');
    $('.sorteerMenu').removeClass('hidden');
  }
  
}

search();