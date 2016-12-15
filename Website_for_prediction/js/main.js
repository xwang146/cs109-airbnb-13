//get user predictors from index page
//run the model and print the result in the prediction p

function predict(){
    // got the user input in every field

    var property_type = $('#property_type input:radio:checked').val();
    var room_type = $('#room_type input:radio:checked').val();
    var bed_type = $('#bed_type input:radio:checked').val();
    console.log(property_type);
    console.log(room_type);
    console.log(bed_type);

    var accommodate = document.getElementById('accommodates').value;
    console.log("here");
    console.log(accommodate);




}

$(document).ready(function() {
  //Resize iframe to full length
  $('#contentFrame').on("load", function() {
    console.log("adfjakl;djl")
    this.style.height = 500
    this.style.height = this.contentWindow.document.body.scrollHeight + 'px';
    console.log(this.style.height)
  });

  //Animate dropdown
  $('#modelnav li').hover(
    function () {
      $('ul', this).stop().slideDown(200);
    },
    function () {
      $('ul', this).stop().slideUp(200);
    }
  );

  //Fallback for without JS
  $('#modelnav li ul').hide().removeClass('fallback');
});