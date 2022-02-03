import { useQuery } from "@apollo/client";
import { useState } from "react";
import BookDetails from "./BookDetails";
import { getBooksQuery } from "../queries/queries";

function BookList() {
  const { error, data } = useQuery(getBooksQuery);
  const [bookid, setBookId] = useState("");
  //   const showBookDetail = (id) => {
  //     graphql()
  //     const { error: bookerror, data: bookdata } = useQuery(getBooksQuery);
  //     console.log(bookdata)
  //   };

  if (data) {
    return (
      <>
        <div id="book-list">
          <ul>
            {data.books.map((book) => (
              //key prop is used by react to check state of element whether
              //re rendering is required or not
              <li key={book.id} onClick={() => setBookId(book.id)}>
                {book.name}
              </li>
            ))}
          </ul>
        </div>
        <div>
          <h3>Book Details</h3>
          {bookid && <BookDetails bookid={bookid} />}
        </div>
      </>
    );
  } else {
    if (error) {
      console.log(error);
    }
    return (
      <div id="book-list">
        <ul>
          <li>Loading books</li>
        </ul>
      </div>
    );
  }
}

export default BookList;
