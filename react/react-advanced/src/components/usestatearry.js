import React, { useState } from 'react'
import { Link } from 'react-router-dom'

import { arraydata } from './data'

const UseStateArray = () => {
    const [data, setData] = useState(arraydata)
    const removeId = (id) => {
        let newdata = data.filter((value) => value.id !== id)
        setData(newdata)
    }

    return (
        <div className="container">
            {data.map((value) => {
                const { id, name } = value
                return (
                    <div key={id} className="item">
                        <h4>{name}</h4>
                        <Link to={`/person/${id}`}>Learn More</Link>
                        <button onClick={() => removeId(id)}>Remove</button>
                    </div>
                )
            })}
            <div>
                <button className="btn" onClick={() => setData([])}>Clear Items</button>
            </div>
        </div>
    )
}

export default UseStateArray