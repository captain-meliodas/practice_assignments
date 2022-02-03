const express = require('express')
const User = require('../models/user') //model for creating users
const routers = new express.Router()

const auth = require('../middleware/auth') //express middleware
    // const { sendWelcomeEmail, sendCancelationEmail } = require('../emails/account') //emails functions

routers.get('/users', auth, (req, res) => {
    // User.find({}).then((users) => {
    //     res.send(users)
    // }).catch((error) => {
    //     res.status(400).send(error)
    // })
    //all checks has been made at middleware
    res.send(req.user)
})


routers.post('/users', async(req, res) => {
    const user = new User(req.body) //creating the user with json parsed data
    try {
        await user.save() //saving the user
            // sendWelcomeEmail(user.email, user.name) //sending welcome email
        const token = await user.generateAuthToken()
        res.status(201).send({ user, token })
    } catch (e) {
        res.status(400).send(e)
    }
})

routers.post('/user/login', async(req, res) => {
    try {
        //findbycreds is a schema mehtod therefore define as 
        //userSchema.statics.findByCreds = async(email, password) --> here no need of binding this using arrow function

        //generateAuthToken is a mehtod called by object therefore define as 
        //userSchema.methods.generateAuthToken = async function() --> need of binding user as this therefore 
        //traditonal function declaration is used 
        const user = await User.findByCreds(req.body.email, req.body.password)
        const token = await user.generateAuthToken()
        if (!user) {
            return res.send({ 'error': 'User not found' })
        }
        res.send({ user, token })
    } catch (e) {
        res.status(404).send({ 'error': 'Something went wrong' })
    }

})

routers.get('/users/:id', (req, res) => {
    User.findById(req.params.id).then((user) => {
        if (!user) {
            return res.status(404).send({ "message": "No user with existing id found" })
        }
        res.send(user)
    }).catch((e) => {
        res.send(e)
    })
})

routers.patch("/users/:id", async(req, res) => {
    const updates = Object.keys(req.body)
    const allowedUpdates = ['name', 'email', 'password', 'age']
    const isValidOperation = updates.every((update) => allowedUpdates.includes(update))

    if (!isValidOperation) {
        return res.status(400).send({ error: 'Invalid updates!' })
    }

    try {
        const user = await User.findById(req.params.id)
        updates.forEach((update) => user[update] = req.body[update])
        await user.save()

        if (!user) {
            return res.status(404).send()
        }

        res.send(user)
    } catch (e) {
        res.status(400).send(e)
    }
})

routers.delete("/users/:id", async(req, res) => {
    try {
        const user = await User.findByIdAndDelete(req.params.id)
        if (!user) {
            return res.status(404).send({
                "message": "No user found to update"
            })
        }
        // sendCancelationEmail(req.user.email, req.user.name) //sending the cancellation message
        res.send(user)

    } catch (e) {
        res.status(404).send(e)
    }
})

module.exports = routers