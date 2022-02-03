Hooks
 - useQuery
     - When we need to just get the data without passing data to api.
 - useMutation
     - When needs to pass some varibales.

typDefs
     - type Query
         - These need resolvers to return the data.
     - input
     - enum
     - Subscriptions
     - custom define using type
         - can also define built in scalar type or user defined type using 'type' .


import {buildSchema} from 'graphql'

const schema = buildSchema(`
    type Course {
        id: ID
        courseName: String!
        price: Int!
        email: String
        stack: Stack
        teachingAssits: [TeachAssist]
    }

    type TeachAssist {
        firstName: String!
        lastName: String!
        experience: Int!
    }

    enum Stack {
        WEB
        MOBILE
        OTHER
    }

    type Query {
        getCourse(id: ID): Course
    }

    input CourseInput {
        id: ID
        courseName: String!
        price: Int!
        email: String
        stack: Stack
        teachingAssits: [TeachAssistInput]
    }

    input TeachAssistInput {
        firstName: String!
        lastName: String!
        experience: Int!
    }

    type Mutation {
        createCourse(input: CourseInput): Course
    }


`)

#resolver function for above typeDefs
const resolvers = {
    getCourse: ({ id }) => {
        return Course(id, courseArgs) #your course object with args format you created
    }
    createCourse: ({ courseProps }) => {
        return new Course(id, courseProps)
    }
}