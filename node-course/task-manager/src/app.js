const express = require('express')
require('./db/mongoose') //only require bcz have code to connect with database

//import all routes to api's for tasks and users
const userRouter = require("./routers/user_routers")
const taskRouters = require("./routers/tasks_routers")

const app = express()

app.use(express.json())

//registring routes of the api's located in task_routers and user_routers
app.use(userRouter)
app.use(taskRouters)

module.exports = app