//REDIS_HOST and REDIS_PORT should be available in deployment environment variable
module.exports = {
    redisHost: process.env.REDIS_HOST,
    redisPort: process.env.REDIS_PORT,
    pgUser:process.env.PGUSER,
    pgHost: process.env.PGHOST,
    pgDatabase: process.env.PGDATABASE,
    pgPassword: process.env.PGPASSWORD,
    pgPort: process.env.PGPORT
}