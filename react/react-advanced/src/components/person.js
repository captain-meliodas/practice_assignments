import React, { useState, useEffect } from 'react'
import { Link, useParams } from 'react-router-dom'

import { arraydata } from './data'

const Person = () => {
    // console.log(useParams())

    // useParams contains values passing through url route
    const { id } = useParams()
    const [person, setPerson] = useState({ id: -11, name: 'Dummy Name' })
    
    //id param is passed as string
    const person_obj = arraydata.find((user) => user.id === parseInt(id))
    useEffect(() => {
        setPerson(person_obj)
    }, [])
    return (
        <div className="container">
            <h2>{person.name}</h2>
            <Link to='/usestatearray'> Back To Example</Link>
        </div>
    )
}

export default Person
