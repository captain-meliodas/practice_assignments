import React, { useState } from 'react'

const Form = () => {
    //you can use useState({firstName:'',email:''}) object instead of having multiples
    // usestates for email and firstname
    const [email, setEmail] = useState('')
    const [firstname, setFirstName] = useState('')
    const [people, setPeople] = useState([])

    const handleSubmit = (ev) => {
        ev.preventDefault()
        if (firstname && email) {

            //calling it as a function so that if clicked multiple times it should always work
            setPeople((people) => {
                let newpeople = [
                    ...people,
                    {
                        firstname,
                        email
                    }
                ]
                return newpeople
            })

            //clearing inputs
            setFirstName("")
            setEmail("")
        }
        else {
            alert("Name and email can't be empty")
        }
    }

    const removeIndex = (index) => {
        let newarray = [...people]
        newarray.splice(index,1)
        setPeople(newarray)
    }

    return (
        <>
            <article style={{ marginTop: '2rem' }}>
                <form className="form" onSubmit={handleSubmit}>
                    <div className="form-control">
                        <label htmlFor="firstName">Name : </label>
                        <input
                            type="text"
                            id="firstName"
                            name="firstName"
                            value={firstname}
                            onChange={(ev) => setFirstName(ev.target.value)} />
                    </div>
                    <div className="form-control">
                        <label htmlFor="email">Email : </label>
                        <input
                            type="text"
                            id="email"
                            name="email"
                            value={email}
                            onChange={(ev) => setEmail(ev.target.value)}
                        />
                    </div>
                    <button type="submit"> Add Person </button>
                </form>

                {people.map((user, index) => {
                    const { id, firstname, email } = user

                    return (
                        <div key={index} className="item">
                            <h4>{firstname}</h4>
                            <p>{email}</p>
                            <button onClick={() => removeIndex(index)}>Remove</button>
                        </div>
                    )
                })}
            </article>
        </>
    )
}

export default Form