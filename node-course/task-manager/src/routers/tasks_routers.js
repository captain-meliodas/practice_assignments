const express = require('express')
const Task = require('../models/tasks') //model for creating tasks
const routers = new express.Router()

routers.post('/tasks', (req, res) => {
    const task = new Task(req.body) //creating the task with json parsed data

    task.save().then(() => { //saving the task
        res.send(task) //sending the response return by mongoose after creating the task
    }).catch((e) => {
        res.status(400).send(e) //error  message if create promise is rejected with status 400
    })
})

routers.get('/tasks', (req, res) => {
    Task.find({}).then((tasks) => {
        res.send(tasks)
    }).catch((error) => {
        res.status(400).send(error)
    })
})

routers.get('/tasks/:id', (req, res) => {
    Task.findById(req.params.id).then((task) => {
        if (!task) {
            return res.status(404).send({ "message": "No Task with existing id found" })
        }
        res.send(task)
    }).catch((e) => {
        res.send(e)
    })
})

module.exports = routers