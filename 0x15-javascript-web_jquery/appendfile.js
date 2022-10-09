function appendList () {
  $.get("dummy.html", function(places) {
    $(".my_list").append(places)
  })
}

$("#add_item").bind("click", appendList)

