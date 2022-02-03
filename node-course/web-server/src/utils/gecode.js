const request = require("request")

const geocode = (address,callback) => {
    const url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${address}.json?access_token=pk.eyJ1IjoicGFkYXI1ODc0OCIsImEiOiJja3RqbDJmd3UxY3ViMnFubGdyODIxaTNvIn0.HjwetRxWdkXjNQ0o9Bj0FQ`

    request({url:url,json:true},(error,response) => {
        if(error){
            callback('Unable to find location',undefined)
        }else if(response.body.features.length === 0){
            callback('Unable to find location try another search',undefined)
        }
        else{
            callback(undefined,{
                latitude: response.body.features[0].center[1],
                longitude: response.body.features[0].center[0],
                location:response.body.features[0].place_name
            })
        }
    })
}
defaults = {
    geocode:geocode
}
module.exports = defaults