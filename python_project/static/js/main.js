const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);


function adjustHeader()
{
    var windowWidth = $(window).width();
    if(windowWidth > 0) {
        if ($(document).scrollTop() >= 100) {
            if($('.header-shrink').length < 1) {
                $('.sticky-header').addClass('header-shrink');
            }
            if($('.do-sticky').length < 1) {
                $('.company-logo img').attr('src', '../static/img/dmc9.svg');
            }
        }
        else {
            $('.sticky-header').removeClass('header-shrink');
            if($('.do-sticky').length < 1 && $('.fixed-header').length == 0 && $('.fixed-header2').length == 0) {
                $('.company-logo img').attr('src', '../static/img/dmc9.svg');
            } else {
                $('.company-logo img').attr('src', '../static/img/dmc9.svg');
            }
        }
    } else {
        $('.company-logo img').attr('src', '../static/img/dmc9.svg');
    }
}