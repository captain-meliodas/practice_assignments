//REDIS_HOST and REDIS_PORT should be available in deployment environment variable
module.exports = {
 redisHost: process.env.REDIS_HOST,
 redisPort: process.env.REDIS_PORT
}