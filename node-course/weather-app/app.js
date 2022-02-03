const gecode = require('./gecode')
const forecast = require('./forecast')

let address = process.argv[2]

if (address) {//call gecode to fetch cordinates of address
    gecode.gecode(address, (error, geocodes) => {
        if (error) {
            return console.log(error)
        }
        console.log(error)
        console.log(geocodes)

        //find weather using lat long (weatherstack api)
        //callback chaining
        forecast(geocodes, (error, forecastdata) => {
            if (error) {
                return console.log(error)
            }
            console.log(error)
            console.log(forecastdata)
        })
    })
}
else {
    console.log("Please specify the address");
}
