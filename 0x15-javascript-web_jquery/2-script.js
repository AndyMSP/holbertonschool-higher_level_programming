function turnRed () {
  $(this).css('color', '#FF0000');
}

$('#red_header').bind('click', turnRed);
