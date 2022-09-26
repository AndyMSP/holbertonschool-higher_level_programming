function addRedClass () {
    $(this).addClass('red')
}

$('#red_header').bind('click', addRedClass);