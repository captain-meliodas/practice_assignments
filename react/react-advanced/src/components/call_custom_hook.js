import React from 'react'

// custom hook
import { useFetch } from './custom_hook'

const url = "https://api.github.com/users"
const Example = () => {
    const { loading, data } = useFetch(url)
    return (
        <div className="container">
            <h3>{loading ? 'loading....' : <List users={data} />}</h3>
        </div>
    )
}

const List = ({ users }) => {
    return (
        <ul className="users">
            {users.map((user) => {
                const { id, login, avatar_url, html_url } = user
                return (
                    <li key={id}>
                        <img src={avatar_url} alt={login} />
                        <div>
                            <h4>{login}</h4>
                            <a href={html_url} target="_blank" rel="noopener noreferrer">Profile</a>
                        </div>
                    </li>
                )
            })}
        </ul>
    )
}

export default Example
