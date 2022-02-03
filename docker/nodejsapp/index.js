//require main express package
const express = require('express')

//creating the app object
const app = express();

//creating a route to home '/' and sending some text to browser
app.get('/', (req, res) => {
    res.send("Response from the node server");
});

//listening to http port '8080' and logging something in response
app.listen(8080, () => {
    console.log("The port 8080 is listening");
});