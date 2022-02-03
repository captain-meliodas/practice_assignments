import React, { useState } from 'react'

const UseStateBasics = () => {
    const [title, setTitle] = useState("Default Title")
    const changeTitle = () => {
        if (title === 'Default Title') {
            setTitle('Title Changed')
        }
        else {
            setTitle('Default Title')
        }

    }
    return (
        <div className="container">
            <h1>{title}</h1>
            <button className="btn" onClick={changeTitle}>Change Title</button>
        </div>
    )

}

export default UseStateBasics