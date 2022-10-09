function toggleColorClass () {
  $('header').toggleClass('green');
  $('header').toggleClass('red');
}

$('#toggle_header').bind('click', toggleColorClass);
