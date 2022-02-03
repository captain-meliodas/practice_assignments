//require main express package
const express = require('express');
const redis = require('redis');

//creating the app object
const app = express();

//creating the redis server client
const client = redis.createClient({
    host:"redis-server",
    port:6379
});

//setting a global variable visits
client.set('visits', 0);

//creating a route to home '/' and sending some text to browser
app.get('/', (req, res) => {
    client.get('visits', (err,visits) => {
        res.send("Response from the node server" + visits);
        client.set('visits', parseInt(visits)+1);
    });
});

//listening to http port '8080' and logging something in response
app.listen(8080, () => {
    console.log("The port 8080 is listening");
});