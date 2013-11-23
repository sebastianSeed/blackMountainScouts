 
  
$(document).ready(function() {

    $('.map').parent().append("<div id='{{event.id}}' style='width:380px; height:200px; margin: 20px; margin-left: 105px;' ></div>");

    var latlng = new google.maps.LatLng(-34.397, 150.644);
    var myOptions = {
      zoom: 15,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    
    
    var map = new google.maps.Map(document.getElementById("map_canvas"),  myOptions);
 

    $('#id_address').change(function() {
      updateMapPosition(map);
    });

    // on load update map if address is not empty 
    if ($('#id_address').val()) {
      updateMapPosition(map);
    }
    
});


 
function updateMapPosition(map) {
  var geocoder = new google.maps.Geocoder();
  var position = geocoder.geocode({'address': $('#id_address').val()} ,
    function(results,status) { 
      if (status == google.maps.GeocoderStatus.OK) {
        if (status != google.maps.GeocoderStatus.ZERO_RESULTS) {
          map.setCenter(results[0].geometry.location);
          var marker = new google.maps.Marker({map:map, position:results[0].geometry.location});
        }
      }
      else {
        alert("Address invalid for google maps please check the address os correct eg suburb and state.");
      }
    }
  );
}
