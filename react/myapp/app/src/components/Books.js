import React from 'react'

import { books } from '../demo/bookdemo'

function Books() {
    return (
        <React.Fragment>
            <section className="book-container">
                
                {books.map((book) => {
                    // <Book key={book.id} author={book.author} title={book.title} img={book.img}/>
                    return <Book key={book.id} {...book} />
                })}
            </section>
        </React.Fragment>
    )
}

const Book = (props) => {
    const { img, title, author, children } = props
    const showTitle = () => {
        // console.log(title);
    }

    return (
        <div className="book-details" onMouseOver={() => showTitle()}>
            <div className="img-container">
                <img src={img} alt={title} />
            </div>
            <div className="book-information">
                <p className="title">
                    {title}
                </p>
                <p className="author">
                    {author}
                </p>
                {children}
            </div>
        </div>
    )
}

export default Books
