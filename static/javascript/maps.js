let $map = document.querySelector('#map')


class MapBox {
    constructor() {
        this.map = null
    }

    async load(){
        mapboxgl.accessToken = 'pk.eyJ1IjoibmFzc2ltOTUxIiwiYSI6ImNrYzI5ODM4ZjIxZHEyd214czE1Y2draXUifQ.vb6BRjY6H2EOmgSlU5fBdA';
        var map = new mapboxgl.Map({
            container: 'map',
            style: 'mapbox://styles/nassim951/ckcaitjh04rsw1ipe4qjf5rz2', // style URL
            center: [2.333333, 48.866667],
            zoom: 10
          });

          map.on('click', function(e) {
            var features = map.queryRenderedFeatures(e.point, {
              layers: ['maraude']
            });
            if (!features.length) {
              return;
            }
          
            var feature = features[0];
          
            var popup = new mapboxgl.Popup({ offset: [0, -15] })
              .setLngLat(feature.geometry.coordinates)
              .setHTML('<h3>' + feature.properties.title + '</h3><p>' + feature.properties.description + '</p>')
              .addTo(map);
          });

           // Add zoom and rotation controls to the map.
           map.addControl(
            new MapboxGeocoder({
            accessToken: mapboxgl.accessToken,
            mapboxgl: mapboxgl
            })
            );

        }
        
}
// VERSION AVEC MAPS
class GoogleMap {

    constructor() {
        this.map = null
        this.bound = null
    }
    /**
     * Charge la carte sur un element
     * @param {HTMLElement} element 
     */
    async load(element){
        return new Promise((resolve, reject) => {
        $script('https://maps.googleapis.com/maps/api/js?', () => {
                    // Centre de la carte => ici IDF
                let center = {lat: 48.866667, lng: 2.333333};
                // Carte centrer sur "center"
                // TODO centrer la carte sur la localisation 
                this.map = new google.maps.Map(
                element, {zoom: 11, center: center  });
            this.bounds = new google.maps.LatLngBounds()
            resolve()
            })
            
        })
        
    }

    /**
     * Ajoute un marker sur la carte
     * @param {string} lat 
     * @param {string} lng 
     */
    addMarker (lat, lng){
        let point = new google.maps.LatLng(lat, lng)
    // Creer un marker avec les donnee de "point"
    let marker = new google.maps.Marker({
        position: point, 
        map: this.map
    })
    this.bounds.extend(point)
    }

    /**
     * centre la map pour englober les markers
     */
    centerMap(){
        this.map.panToBounds(this.bounds)
        this.map.fitBounds(this.bounds)
    }
}

const initMap = async function (){
    let map = new MapBox()
    await  map.load($map)
    // Array.from(document.querySelectorAll('.item')).forEach(element => {
    //     map.addMarker(item.dataset.lat, item.dataset.lng)
    // })   
    // map.centerMap()
}

if ($map !== null) {
    initMap()
}