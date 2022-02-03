const mongoose = require("mongoose")

mongoose.connect('mongodb://127.0.0.1:27017/tasks-manager-db', {
    useNewUrlParser: true,
})

//setting custom validation to days field
const Task = mongoose.model('Task', {
    description: {
        type: String
    },
    completed: {
        type: Boolean
    },
    days: {
        type: Number,
        validate(value) {
            if (value <= 0) {
                throw new Error("Number of days should be atleas 1")
            }
        }
    }
})

const Data1 = new Task({
    description: 'Practicing Mongoose Lib',
    completed: true
})

//if callback not provided it will return promise
//resolving and rejecting promise based on condition what returns
Data1.save().then((res) => {
    console.log(res)
}).catch((error) => {
    console.log(res)
})