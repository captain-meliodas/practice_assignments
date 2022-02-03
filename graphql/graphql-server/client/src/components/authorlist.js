import React, { useState } from "react";
import { useQuery, useMutation } from "@apollo/client";
import {
  getAuthorsQuery,
  addBookMutation,
  getBooksQuery,
} from "../queries/queries";

function AuthorList() {
  const { error, data } = useQuery(getAuthorsQuery);
  const [addBookHook, info] = useMutation(addBookMutation);
  // Declare a new state variable, and there hooks
  const [bookname, setBookname] = useState();
  const [genre, setGenre] = useState();
  const [authorid, setAuthorid] = useState();

  const handleSubmit = (ev) => {
    ev.preventDefault();
    addBookHook({
      variables: {
        name: bookname,
        genre: genre,
        authorid: authorid,
      },
      refetchQueries: [{ query: getBooksQuery }],
    });
    setBookname("");
    setGenre("");
    setAuthorid(0);
    console.log(info);
  };

  if (data) {
    return (
      <form id="choose_book" onSubmit={handleSubmit}>
        <div>
          <label>Book Name</label>
          <input
            name="book"
            placeholder="Book Name"
            onChange={(e) => setBookname(e.target.value)}
          />
        </div>
        <div>
          <label>Genre</label>
          <input
            name="genre"
            placeholder="Genre"
            onChange={(e) => setGenre(e.target.value)}
          />
        </div>

        <div id="author-list">
          <label>Author Name</label>
          <select id="author" onChange={(e) => setAuthorid(e.target.value)}>
            <option value="0">Select Author</option>
            {data.authors.map((author) => (
              //key prop is used by react to check state of element whether
              //re rendering is required or not
              <option value={author.id} key={author.id}>
                {author.name}
              </option>
            ))}
          </select>
        </div>
        <button type="submit" id="form_btn">
          {" "}
          Add{" "}
        </button>
      </form>
    );
  } else {
    if (error) {
      console.log(error);
    }
    return (
      <div id="author-list">
        <ul>
          <li>Loading authors</li>
        </ul>
      </div>
    );
  }
}

export default AuthorList;
