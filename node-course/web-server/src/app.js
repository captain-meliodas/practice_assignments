const express = require('express')
const path = require('path')
const hbs = require('hbs')
const geocode = require('./utils/gecode')
const forecast = require('./utils/forecast')

const app = express()
// console.log(__dirname)
// console.log(__filename)
const staticFiles = path.join(__dirname, '../public') //public directory
const viewsPath = path.join(__dirname, '../templates/views') //views path
const partialsPath = path.join(__dirname, '../templates/partials') //views path
app.use(express.static(staticFiles)) //serving static file (by defautl index.html is served from file)

//setting the view engine (templating engine)
app.set('view engine', 'hbs')
app.set('views', viewsPath)
hbs.registerPartials(partialsPath)

//no need as we have index.html setuped
app.get('', (req, res) => {
    res.render("index", {
        title: 'Weather Application',
        name: 'GS Labs'
    })
})

app.get('/about', (req, res) => {
    res.render("about", {
        title: 'Weather Application About',
        name: 'GS Labs'
    })
})

app.get('/weather', (req, res) => {
    if (!req.query.address) {
        return res.send({
            'status': 404,
            'error': 'No address has been provided'
        })
    }

    geocode.geocode(req.query.address, (error, coordinates) => {
        if (error) {
            return res.send({
                'status': 500,
                'error': 'Internal server error'
            })
        }
        else {
            const { latitude, longitude, location } = coordinates
            forecast(coordinates, (error, data) => {
                if (error) {
                    return res.send({
                        'status': 500,
                        'error': 'Internal server error'
                    })
                }
                else {
                    return res.send({
                        'status': 200,
                        latitude,
                        longitude,
                        location,
                        'weather': data
                    })
                }
            })
        }
    })
})
//wild card routes
app.get('/about/*', (req, res) => {
    res.render("about", {
        title: '404',
        name: 'GS Labs',
        errorMessage: 'Page not found'
    })
})

app.get('*', (req, res) => {
    res.render("404", {
        title: '404',
        name: 'GS Labs',
        errorMessage: 'Page not found'
    })
})

app.listen(3000, () => {
    console.log("server started")
})