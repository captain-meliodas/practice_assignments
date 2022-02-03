import React, { useState, useContext } from 'react'

const data = [
    { id: 1, name: "Jhon Doe" },
    { id: 2, name: "Mark Demo" },
    { id: 3, name: "Tony Stark" }
]

//context
//it contains two components producer and consumer
const PersonContext = React.createContext()

const ContextApi = () => {
    const [people, setPeople] = useState(data)

    //removeperson is required in single person component
    //now we are passing it through useContext
    const removePerson = (id) => {
        setPeople((people) => {
            return people.filter((person) => person.id !== id)
        })
    }
    //wrapping all elements in provider to provide the removePerson in context
    //can be called using useContext(PersonContext)
    return (
        <PersonContext.Provider value={{ removePerson }}>
            <section className="container">
                <h3>Using Context API</h3>
                <List people={people} />
            </section>
        </PersonContext.Provider>
    )
}

const List = (props) => {
    const { people } = props
    return (
        <>
            {people.map((person) => {
                return (
                    < SinglePerson key={person.id} person={person} />
                )
            })}
        </>
    )
}

const SinglePerson = ({ person }) => {
    const { id, name } = person
    const { removePerson } = useContext(PersonContext)
    return (
        <div className="item">
            <h4>{name}</h4>
            <button onClick={() => removePerson(id)} >Remove</button>
        </div>
    )
}

export default ContextApi
