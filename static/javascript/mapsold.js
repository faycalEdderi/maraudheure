let $map = document.querySelector('#map')

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
    // centerMap(){
    //     this.map.panToBounds(this.bounds)
    //     this.map.fitBounds(this.bounds)
    // }
}

const initMap = async function (){
    let map = new GoogleMap()
    await  map.load($map)
    Array.from(document.querySelectorAll('.item')).forEach(element => {
        map.addMarker(item.dataset.lat, item.dataset.lng)
    })   
    // map.centerMap()
}

if ($map !== null) {
    initMap()
}