// crud --> create read update delete
const mongodb = require("mongodb")
const { MongoClient, ObjectID } = mongodb
// const MongoClient = mongodb.MongoClient
// const ObjectID = mongodb.ObjectId //to get the object id from object string 
//-----------------------------------in mongo db id is stored as string 
//-----------------------------------we need to convert that string into hex using ObjectID
//---------------------------------- in order to search using id
// const id = new ObjectId("your_db_object_string")

const connectioURL = 'mongodb://127.0.0.1:27017'

const dbName = 'task-manager'

MongoClient.connect(connectioURL, { useNewUrlParser: true }, (error, client) => {
    if (error) {
        return console.log("Unable to connect to db server", error)
    }
    const db = client.db(dbName)
        // db.collection('users').insertOne({
        //     name: 'John Doe',
        //     age: '26'
        // })
    db.collection('users').findOne({
        name: 'John Doe',
        age: '26'
    }, (error, user) => {
        console.log(user)
    })
    db.collection('users').find({
        age: '26'
    }).toArray((error, ids) => {
        console.log(ids)
    })
})