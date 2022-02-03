const path = require('path')
const http = require('http')
const express = require('express')
const socketio = require('socket.io')

const app = express()
const server = http.createServer(app)
const io = socketio(server)

const port = process.env.PORT || 3000
const publicDirectoryPath = path.join(__dirname, '../public')

//custom libs
const { generateMessage } = require("./utils/message")
const { addUser, getUser, getUsersInRoom, removeUser } = require("./utils/users")

app.use(express.static(publicDirectoryPath))

// let count = 0

io.on('connection', (socket) => {

    // socket.on('increment', () => {
    //     count++
    //     socket.emit('countUpdated', count) // emits the connection to specific client who emits the connection
    //     io.emit('countUpdated', count) //emits the connection to all available client
    // })

    socket.on('emit_from_client', (message, callback) => {
        if (message == '') {
            return callback(true) //to send acknowledgement to the client (emitter)
        }
        const user = getUser(socket.id)
        const response = {
            ...generateMessage(message),
            ...user
        }
        io.emit('emit_from_server', response)
        callback("Delivered")

    })

    //options --> { username, room }
    // ... is a spread operator to paste all fields inside the object
    socket.on('join', (options, callback) => {
        const { username, room } = options
        const { error, user } = addUser({
            id: socket.id,
            ...options
        })

        if (error) {
            //send ack that user hasn't joined due to error
            return callback(error)
        }

        socket.join(room) //no one can see messages from other room's

        const response = {
            ...generateMessage('Welcome'),
            username: 'Admin'
        }

        socket.emit('emit_from_server', response) // 'Emit by the server to only initiator (client)'

        // socket.broadcast.emit('emit_from_server', generateMessage('A new user has joined')) //'Emitted to all clients except the initiator (client)'
        // .to here specify the room (isolate) name in which we have to circulate messages
        socket.broadcast.to(room).emit('emit_from_server', {...generateMessage(`${username} has joined`), username: 'Admin' })

        io.to(room).emit('roomData', {
            room: room,
            users: getUsersInRoom(room)
        })

        //if user is successfully joined the room 
        // callback ack with no error (empty arguments)
        callback()
    })

    socket.on('sendLocation', (coords, callback) => {
        const user = getUser(socket.id)
        const message = `https://google.com/maps?q=${coords.latitude},${coords.longitude}`
        const response = {
            ...generateMessage(message),
            ...user
        }
        io.to(user.room).emit('clientLocation', response)
        callback()
    })

    socket.on('disconnect', () => {
        const user = removeUser(socket.id)
        if (user) {
            io.to(user.room).emit('emit_from_server', generateMessage(`${user.username} has left`))
            io.to(user.room).emit('roomData', {
                room: user.room,
                users: getUsersInRoom(user.room)
            })
        }
    })
})

server.listen(port, () => {
    console.log(`Server is up on port ${port}!`)
})