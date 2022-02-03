import { gql } from "@apollo/client";

//query
const getBooksQuery = gql`
  {
    books {
        id
        name
      }
  }
`;

const getAuthorsQuery = gql`
  {
    authors {
        id
        name
      }
  }
`;

const addBookMutation = gql`
  mutation addBook($name : String! ,$genre: String! ,$authorid : ID!){
    addBook(name : $name,genre: $genre,authorid : $authorid){
      name,
      author {
        name
      }
    }
  }`

const getBookQuery = gql`
  query Book($id : ID!){
    book(id:$id){
      id,
      name,
      genre
      author {
        id
        name
        books{
          id
          name
        }
      }
    }
  }`

export {
  getBooksQuery,
  getAuthorsQuery,
  addBookMutation,
  getBookQuery
}