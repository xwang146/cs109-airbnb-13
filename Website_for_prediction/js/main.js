//get user predictors from index page
//run the model and print the result in the prediction p

function predict(){
    // get the user input in every field
    var userInput = {
      'longitude': $('#Lon').text(),
      'latitude': $('#Lat').text(),
      'accommodates': $('#accommodates').val(),
      'bedrooms': $('#bedrooms').val(),
      'bathrooms': $('#bathrooms').val(),
      'beds': $('#beds').val(),
      'property_type_0': +($('#property_type input:radio:checked').val() == '0'),
      'property_type_1': +($('#property_type input:radio:checked').val() == '1'),
      'property_type_2': +($('#property_type input:radio:checked').val() == '2'),
      'room_type_0': +($('#room_type input:radio:checked').val() == '0'),
      'room_type_1': +($('#room_type input:radio:checked').val() == '1'),
      'room_type_2': +($('#room_type input:radio:checked').val() == '2'),
      'bed_type_0': +($('#bed_type input:radio:checked').val() == '0'),
      'bed_type_1': +($('#bed_type input:radio:checked').val() == '1'),
      'bed_type_2': +($('#bed_type input:radio:checked').val() == '2'),
      'bed_type_3': +($('#bed_type input:radio:checked').val() == '3'),
      'bed_type_4': +($('#bed_type input:radio:checked').val() == '4')
    };

    $('#output').html("Processing...");

    //get the output
    $.ajax({
      url: 'https://vundha2hjh.execute-api.us-east-1.amazonaws.com/prod/predict',
      type: 'get',
      data: userInput,
      success: function(response) {
        $('#output').html('$' + Math.round(parseFloat(response)))
      },
      error: function(xhr) {
        console.log('Prediction Error')
        console.log(xhr)
      }
    });
}

//Modeling (ipynb) section navbar
$(document).ready(function() {
  //Resize iframe to full length
  $('#contentFrame').on("load", function() {
    this.height = this.contentWindow.document.body.scrollHeight + 'px';
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
//End modeling navbar

//Longitude and latitude selector
var map = L.map('map').setView([40.712784, -74.005941], 11).on('click', function(e) {
  $('#Lon').html(e.latlng.lng.toFixed(4));
  $('#Lat').html(e.latlng.lat.toFixed(4));
});

L.Icon.Default.imagePath = 'images/';

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);