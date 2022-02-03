import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import BookList from './components/booklist';
import AuthorList from './components/authorlist';
import reportWebVitals from './reportWebVitals';
import {
  ApolloClient,
  InMemoryCache,
  ApolloProvider,
} from "@apollo/client";


const client = new ApolloClient({
  uri: "http://127.0.0.1:4000/graphql",
  cache: new InMemoryCache()
});

ReactDOM.render(
  // <React.StrictMode>
  <ApolloProvider client={client}>
    <div id="Main">
      <h1>Ninja's Reading List</h1>
      <BookList />
      <AuthorList/>
    </div>
    <App />
  </ApolloProvider>,
  // </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
