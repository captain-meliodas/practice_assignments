const mongoose = require('mongoose')

mongoose.connect(process.env.MONGODB_SERVER)

mongoose.connection.once('open', () => {
    console.log('connected to db')
})