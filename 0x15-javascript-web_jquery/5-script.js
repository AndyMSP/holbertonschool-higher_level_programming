function appendList () {
    $(".my_list").append("<li>Item</li>")
}

$("#add_item").bind("click", appendList)