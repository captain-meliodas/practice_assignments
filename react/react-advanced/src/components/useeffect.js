import React, { useState, useEffect } from 'react'
const url = "https://api.github.com/users"

const UseEffectBasics = () => {
    // const [counter, setCounter] = useState(0)
    // useEffect(() => {
    //     console.log("---------------------------")
    //     document.title = `New Message (${counter})`

    //     return () => {
    //         // cleanup
    //         // runs every time useeffect called
    //     }
    //     // - [] to run only once when page loaded
    //     // - [value] run when there is change in dependent value
    //     // - [condition] when useeffect has to run on certain condtions
    // },[counter])

    const [users,setUsers] = useState([]);

    const getUsers = async() => {
        const response = await fetch(url)
        const users = await response.json()
        setUsers(users)
    }

    useEffect(() => {
        getUsers()
    },[])

    return (
        <div className="container">
            {/* <h1>{counter}</h1> */}
            {/* <button className="btn" onClick={() => setCounter(counter + 1)}>Increase</button> */}
            <h3>Github Users</h3>

            <ul className="users">
                {users.map((user) => {
                    const {id, login, avatar_url, html_url} = user
                    return (
                        <li key={id}>
                            <img src={avatar_url} alt={login}/>
                            <div>
                                <h4>{login}</h4>
                                <a href={html_url} target="_blank" rel="noopener noreferrer">Profile</a>
                            </div>
                        </li>
                    )
                })}
            </ul>
        </div>
    )
}

export default UseEffectBasics