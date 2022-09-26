function turnRed () {
  $(this).css('color', '#FF0000');
}

$('header').bind('click', turnRed);
