function addRedClass () {
    $("header").addClass('red')
}

$('#red_header').bind('click', addRedClass);