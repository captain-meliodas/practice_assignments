import React, { useState } from 'react'

const data = [
    { id: 1, name: "Jhon Doe" },
    { id: 2, name: "Mark Demo" },
    { id: 3, name: "Tony Stark" }
]

const PropDrilling = () => {
    const [people, setPeople] = useState(data)

    //removeperson is required in single person component
    //and we can pass it through propdrilling going one step deeper
    //and passing the function as a props
    const removePerson = (id) => {
        setPeople((people) => {
            return people.filter((person) => person.id !== id)
        })
    }
    return (
        <section className="container">
            <h3>Prop Drilling</h3>
            {/* passing removePerson to next level */}
            <List people={people} removePerson={removePerson} />
        </section>
    )
}

const List = (props) => {
    const { people, removePerson } = props
    
    return (
        <>
            {people.map((person) => {
                {/* passing removePerson to next level */ }
                return (
                    < SinglePerson key={person.id} person={person} removePerson={removePerson} />
                )
            })}
        </>
    )
}

const SinglePerson = ({ person, removePerson }) => {
    const { id, name } = person
    return (
        <div className="item">
            <h4>{name}</h4>
            <button onClick={() => removePerson(id)} >Remove</button>
        </div>
    )
}

export default PropDrilling
