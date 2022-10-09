function sayHello(data) {
  $("#hello").text(data.hello)
  console.log(data)
}

$.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", sayHello)


// $.getJSON("https://fourtonfish.com/hellosalut?callback=?lang=fr", function(data){
//    //response data are now in the result variable
//    console.log(data);
// });

