import React, { useState } from 'react'

const UseStateObject = () => {
    const [object, setObject] = useState({
        name: "Jhon Doe",
        age: 26,
        token: "asdasdapdoah31223qyajakhdlafsdbljkad"
    })
    const UpdateToken = () => {
        setObject({ ...object, token: "guiasgfdaslkfgaslkfasfkjasfg2222" })
    }
    return (
        <div className="container">
            <h1>Use state Object example</h1>
            <h3>{object.name}</h3>
            <h3>{object.age}</h3>
            <h3>{object.token}</h3>
            <button className="btn" onClick={UpdateToken}>Update Token</button>
        </div>
    )

}

export default UseStateObject