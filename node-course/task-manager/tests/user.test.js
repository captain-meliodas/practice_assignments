const request = require("supertest")
const app = require("../src/app")
const User = require("../src/models/user")

const mongoose = require("mongoose")
const jwt = require('jsonwebtoken')


const test_user_id = new mongoose.Types.ObjectId()
const test_token = jwt.sign({ _id: test_user_id }, process.env.JWT_SECRET)

const testuser = {
    "_id": test_user_id,
    "name": "John Doe",
    "email": "jhondoe@gmail.com",
    "password": "jhon12345",
    "tokens": [{
        "token": test_token
    }]
}

//runs before test happens (afterEach runs after tests complete or 
//beforeAll one db request(runs before all test cases (vice-vers -->afterAll)))
beforeEach(async() => {
    await User.deleteMany()
    await new User(testuser).save()
})

test('Signup User Call', async() => {
    await request(app).post('/users').send({
        "name": "Ankit",
        "email": "ankit@gmail.com",
        "password": "ank12345"
    }).expect(201)
})

test('Login user', async() => {
    await request(app).post('/user/login').send({
        email: testuser.email,
        password: testuser.password
    }).expect(200)
})

test('Get User', async() => {
    await request(app).get(`/users/${test_user_id}`).expect(200)
})