//all the config and keys to make a connection with redis is here
const keys = require('./keys');
const redis = require('redis');

const redisClient = redis.createClient({
    host: keys.redisHost,
    port: keys.redisPort,
    retry_strategy: () => 1000
});

const sub = redisClient.duplicate();

function fibonnaci(index) {
    if (index < 2) {
        return 1;
    }
    return fibonnaci(index - 1) + fibonnaci(index - 2)
}

sub.on('message', (channel, message) => {
    redisClient.hset('values', message, fibonnaci(parseInt(message)));
});
sub.subscribe('insert');