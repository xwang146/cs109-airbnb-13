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

    //pass the predictor list to our model
    var price=0;

        $("#output").html("Processing...");



    //get the output


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


var margin = {top: 20, right: 10, bottom: 20, left: 20};
var width = 700 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var padding = 20;

var svg = d3.select("#map").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom);

var map = L.map('map').setView([40.712784, -74.005941], 11).on('click', onMapClick);
L.Icon.Default.imagePath = 'images/';

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

function onMapClick(e) {
    //alert("You clicked the map at " + e.latlng);
    $("#Lon").html(e.latlng.lng);
    $("#Lat").html(e.latlng.lat);

}
