const keys = require('./keys');

//Express App setup
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();

app.use(cors());
app.use(bodyParser.json());

//postgres setup

//making the connection with postgres---
const pg = require('pg');
var conString = `postgres://${keys.pgUser}:${keys.pgPassword}@${keys.pgHost}/${keys.pgDatabase}`;
var client = new pg.Client(conString);
client.connect();
client.on('connect', () => {
    pgClient.query('CREATE TABLE IF NOT EXISTS values (number INT)').catch((err) => console.log(err.stack));
});
client.on('error', () => console.log("Lost connection to postgres"));
//----------------------------------------------------------------
//making pool for making queries to db
const { Pool } = require('pg');
const pgClient = new Pool({
    user: keys.pgUser,
    host: keys.pgHost,
    database: keys.pgDatabase,
    password: keys.pgPassword,
    port: keys.pgPort
});
//----------------------------------------------------------------------

//redis client setup
const redis = require('redis');

//client used for incoming traffic
const redisClient = redis.createClient({
    host: keys.redisHost,
    port: keys.redisPort,
    retry_strategy: () => 1000
});

//client used for making request or invoking worker
const redisPublisher = redisClient.duplicate();

// Express route handlers

app.get('/', (req, res) => {
    res.send("You are at the home page") //just to check whether app is working 
});

app.get('/values/all', async (req, res) => {
    const values = await pgClient.query('SELECT * from values');
    res.send(values.rows);
});

app.get('/values/current', async (req, res) => {
    //return all the values stored in redis cache
    redisClient.hgetall('values', (err, values) => {
        res.send(values);
    });
});

app.post('/values', async (req, res) => {
    const index = req.body.index
    if (parseInt(index) > 40) {
        //do nothing if required to calculate fib seq of large number        
        return res.status(422).send('Entity too large to handle');
    }
    redisClient.hset('values', index, 'Not Calculated'); //set the hash value index:answer
    redisPublisher.publish('insert', index); //this will invoke the worker to insert the index value in redis db
    const query = {
        text: 'INSERT INTO values(number) VALUES($1)',
        values: [parseInt(index)],
    }
    pgClient.query(query, (err, res) => {
        if (err) {
            console.log(err);
        }
        else {
            console.log(res.rows);
        }
    }); //inserting index data into postgres
    res.send({
        index: index,
    });
});

app.listen(8012, err => {
    console.log("Listing to port 8012");
});

