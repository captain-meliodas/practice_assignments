const users = []

//addUser

const addUser = ({ id, username, room }) => {
    //Clean the data
    username = username.trim().toLowerCase()
    room = room.trim().toLowerCase()

    //validate the data
    if (!username || !room) {
        return {
            error: 'Username and room are required to join'
        }
    }

    //Check for existing user in room
    const existingUser = users.find((user) => {
        return user.username === username && user.room === room
    })

    if (existingUser) {
        return {
            error: 'Username is already taken'
        }
    }

    // Store the user

    const user = { id, username, room }
    users.push(user)
    return { user }
}

//removeUser
const removeUser = (id) => {
    // findindex stops searching when index is found
    // filter method searches for pattern till last index
    const index = users.findIndex((user) => user.id === id)

    if (index !== -1) {
        return users.splice(index, 1)[0]
    }
}

//getUser (any User by irrespective of room)
const getUser = (id) => {
    return users.find((user) => user.id === id)
}

//getUsersInRoom (all users in specific room)
const getUsersInRoom = (room) => {
    return users.filter((user) => user.room === room)
}

// addUser({
//     id: 12,
//     username: "Ankit Singh",
//     room: "Room1"
// })

// addUser({
//     id: 13,
//     username: "Bhagyashree",
//     room: "Room2"
// })

// addUser({
//     id: 14,
//     username: "Abhishek",
//     room: "Room2"
// })

// // console.log(users)
// console.log(getUser(13));
// console.log(getUsersInRoom("room2"));

module.exports = {
    addUser,
    getUser,
    getUsersInRoom,
    removeUser
}