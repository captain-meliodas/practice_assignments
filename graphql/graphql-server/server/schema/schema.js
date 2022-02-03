const graphql = require('graphql')
const _ = require('lodash')

const {
    GraphQLObjectType,
    GraphQLString,
    GraphQLID,
    GraphQLInt,
    GraphQLSchema,
    GraphQLList,
    GraphQLNonNull
} = graphql

//models
const Book = require('../models/books')
const Author = require('../models/author')

//demo data
// const books = [
//     { id: '1', name: 'Node Js complete guide', genre: 'Programming', authorid: '2' },
//     { id: '2', name: 'Python Programming', genre: 'Programming', authorid: '2' },
//     { id: '3', name: 'Machine Learning', genre: 'Core Concepts', authorid: '3' },
//     { id: '4', name: 'A tour of JavaScript', genre: 'Web Technologies', authorid: '4' }
// ]
// const authors = [
//     { id: '1', name: 'Cormen', age: 24 },
//     { id: '2', name: 'Forouzan', age: 25 },
//     { id: '3', name: 'Galvin Gange', age: 26 },
//     { id: '4', name: 'Robert Malro', age: 27 }
// ]


const BookType = new GraphQLObjectType({
    name: 'Book',
    fields: () => ({
        id: { type: GraphQLID },
        name: { type: GraphQLString },
        genre: { type: GraphQLString },
        author: {
            type: AuthorType,
            resolve(parent, args) {
                // return _.find(authors, { id: parent.authorid })
                return Author.findById({ _id: parent.authorid })
            }
        }
    })
})

const AuthorType = new GraphQLObjectType({
    name: 'Author',
    fields: () => ({
        id: { type: GraphQLID },
        name: { type: GraphQLString },
        age: { type: GraphQLInt },
        books: {
            type: new GraphQLList(BookType),
            resolve(parent, args) {
                // return _.filter(books, { authorid: parent.id })
                console.log(parent)
                return Book.find({ authorid: parent._id })
            }
        }
    })
})

//Mutations (convert graphiql query to save in db)
const Mutation = new GraphQLObjectType({
    name: 'Mutation',
    fields: {
        addAuthor: {
            type: AuthorType,
            args: {
                name: { type: new GraphQLNonNull(GraphQLString) },
                age: { type: new GraphQLNonNull(GraphQLInt) }
            },
            resolve(parent, args) {
                let author = new Author({
                    name: args.name,
                    age: args.age
                })
                return author.save()
            }
        },
        addBook: {
            type: BookType,
            args: {
                name: { type: new GraphQLNonNull(GraphQLString) },
                genre: { type: new GraphQLNonNull(GraphQLString) },
                authorid: { type: new GraphQLNonNull(GraphQLID) }
            },
            resolve(parent, args) {
                let book = new Book({
                    name: args.name,
                    genre: args.genre,
                    authorid: args.authorid
                })
                return book.save()
            }
        }
    }
})

const RootQuery = new GraphQLObjectType({
    name: 'RootQueryType',
    fields: {
        book: {
            type: BookType,
            args: { id: { type: GraphQLID } },
            resolve(parent, args) {
                //code to get data from db and other source
                // return _.find(books, { id: args.id })
                return Book.findById({ _id: args.id })
            }
        },

        author: {
            type: AuthorType,
            args: { id: { type: GraphQLID } },
            resolve(parent, args) {
                //code to get data from db and other source
                // return _.find(authors, { id: args.id })
                return Author.findById({ _id: args.id })
            }
        },
        books: {
            type: new GraphQLList(BookType),
            resolve(parent, args) {
                // return books
                return Book.find({})
            }
        },
        authors: {
            type: new GraphQLList(AuthorType),
            resolve(parent, args) {
                // return authors
                return Author.find({})
            }
        }
    }
})

module.exports = new GraphQLSchema({
    query: RootQuery,
    mutation: Mutation
})