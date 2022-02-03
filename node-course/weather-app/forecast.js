const request = require('request')

// http://api.weatherstack.com/current
//     ? access_key = YOUR_ACCESS_KEY
//     & query = New York

const forecast = ({latitude:lat,longitude:long},callback) => {
    const url = "http://api.weatherstack.com/current?"
    const access_key = "7eb435225755e69a00e29349bb3bd4f6"
    let final_url = url + "access_key=" + access_key + "&query=" + lat+","+long
    request({ url: final_url, json: true }, (error, response) => {
        if(error){
            callback('Unable to find location',undefined)
        }else if(response.body.error){
            callback('Unable to find location try another search',undefined)
        }
        else{
            callback(undefined,{
                data:response.body.current
            })
        }
    })
}

module.exports = forecast