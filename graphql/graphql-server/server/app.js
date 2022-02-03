//npm dependencies
const express = require('express')
require('dotenv').config({ path: './config/.env' })
const { graphqlHTTP } = require('express-graphql'); //allow express to understand graphql queries
const port = process.env.PORT
var cors = require('cors')

//custom dependencies
const schema = require('./schema/schema')
require('./schema/database')

//app setup
const app = express()
app.use(cors())
app.use('/graphql', graphqlHTTP({
    //whenever /graphql is accessed graphqlHTTP is fired
    schema,
    graphiql: true
}))

app.listen(port, () => {
    console.log('Listening on the port ', port);
})