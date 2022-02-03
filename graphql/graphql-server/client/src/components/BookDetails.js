import { useQuery } from '@apollo/client'
import React from 'react'

import { getBookQuery } from '../queries/queries'

const BookDetails = (props) => {
    const { bookid } = props
    const { error, data } = useQuery(getBookQuery, { variables: { id: bookid } })
    if (data) {
        const { book } = data
        console.log(book.author.books)
        return (
            <div>
                <p>{book.name}</p>
                <p>{book.author.name}</p>
                <p>More Books by author:--</p>
                <ul>
                    {book.author.books.map((item) => {
                        return (
                        <li key={item.id}>
                            {item.name}
                        </li>
                        )
                    })}
                </ul>
            </div>
        )
    }
    return (<div>Loding...........</div>)
}

export default BookDetails
