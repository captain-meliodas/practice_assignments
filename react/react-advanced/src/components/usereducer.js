import React, { useReducer, useState } from 'react'

//reducer setup
const reducer = (state, action) => {
    const { data, type, userId } = action
    if (type === "ADD_PEOPLE") {
        return {
            ...state,
            people: [...state.people, data],
            isModalOpen: true,
            modalContent: `Hi ${data.name}`
        }
    }

    if (type === "CLOSE_MODAL") {
        return {
            ...state,
            isModalOpen: false
        }
    }

    if (type === "REMOVE_USER"){
        let users = state.people.filter((user) => user.id !== userId)
        return {
            ...state,
            people: users,
            isModalOpen: false,
            modalContent:''
        }
    }

    // return state
    throw new Error("No matching action type is found")
}

//reducer default state
const defaultState = {
    people: [],
    isModalOpen: false,
    modalContent: ''
}

const UseReducerBasics = () => {
    const [name, setName] = useState("")
    // const [people,setPeople] = useState([])
    // const [showModal,setShowModal] = useState(false)

    //useReducer takes 2 arguments
    // 1- function (action to be performed if dispatch is invoked)
    // 2- defaultState object variables
    const [state, dispatch] = useReducer(reducer, defaultState)

    const handleSubmit = (ev) => {
        ev.preventDefault()
        if (name) {
            // setShowModal(true)
            // setPeople([...people,{id: new Date().getTime().toString(),name}])
            let action = { type: "ADD_PEOPLE", data: { id: new Date().getTime().toString(), name } }
            setName("")
            dispatch(action)
        }
        else {
            // console.log("name is not provided")
            dispatch({ type: "NO_MATCHING" })
            // setShowModal(true)
        }
    }
    const closeModal = () => {
        dispatch({ type: "CLOSE_MODAL" })
    }

    return (
        <div style={{ position: "relative" }}>
            <form className="form" onSubmit={handleSubmit}>
                {state.isModalOpen && <Modal closeModal={closeModal} modalContent={state.modalContent} />}
                <input
                    type="text"
                    name="firstname"
                    value={name}
                    onChange={(ev) => setName(ev.target.value)} />

                <button type='submit'>add </button>
            </form>
            <div className="container">
                {state.people.map((user) => {
                    return (
                        <div key={user.id} className="item">
                            <h4>{user.name}</h4>
                            <button onClick={() => dispatch({ type: 'REMOVE_USER', userId: user.id })}>Remove</button>
                        </div>
                    )
                })}
            </div>
        </div>
    )
}

//can be in separate file
const Modal = (props) => {
    const { modalContent, closeModal } = props

    setTimeout(() => {
        closeModal();
    }, 3000)

    return (
        <div className="modal" style={{ top: '5rem' }}>
            <p>{modalContent}</p>
        </div>
    )
}

export default UseReducerBasics
