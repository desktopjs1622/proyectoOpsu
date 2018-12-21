(function($) {
    "use strict"; // Start of use strict

    $(window).on('map:init', function (e) {
        geodjango_id_coordenada_edit.geom_type = 'Point';
        geodjango_id_poligonal_edit.geom_type = 'Polygon';
        var detail = e.originalEvent ?
                     e.originalEvent.detail : e.detail,
            mapbox = new L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
                attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
                maxZoom: 18,
                id: 'mapbox.streets',
                accessToken: 'pk.eyJ1IjoiZGNoYXBsaW5za3kiLCJhIjoiY2o3d2p1eWdoNXAzMDJxbnV1ZG05YmF6ZiJ9.tXdY9DfXJiR7t0GgYKMiug'
            }),

            mapbox_sat = new L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
                attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
                maxZoom: 18,
                id: 'mapbox.streets-satellite',
                accessToken: 'pk.eyJ1IjoiZGNoYXBsaW5za3kiLCJhIjoiY2o3d2p1eWdoNXAzMDJxbnV1ZG05YmF6ZiJ9.tXdY9DfXJiR7t0GgYKMiug'
            });

            detail.map.addLayer(mapbox);
            var baseLayers = {
                "Mapa": mapbox,
                "Satelite": mapbox_sat
            };
    
            L.control.layers(baseLayers).addTo(detail.map);

    });
})(jQuery); // End of use strict
