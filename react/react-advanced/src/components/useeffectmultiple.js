
import React, { useState, useEffect } from 'react'

const url = "https://api.github.com/users/captain-meliodas"

function UseEffectMultiple() {
    const [user, setUser] = useState("default user")
    const [isLoading, setIsLoading] = useState(true)
    const [isError, setIsError] = useState(false)

    useEffect(() => {
        fetch(url).then((response) => {
            if (response.status >= 200 && response.status <= 299) {
                return response.json()
            }
            else {
                setIsLoading(false)
                setIsError(true)
                throw new Error(response.statusText)
            }
        }).then((user) => {
            const { login } = user
            setUser(login)
            setIsLoading(false)
        }).catch((error) => {
            console.log(error)
        })
    }, [])

    if (isLoading) {
        return (
            <div className="container">
                <h3>Loading.......</h3>
            </div>
        )
    }
    if (isError) {
        return (
            <div className="container">
                <h3>Internal Server Error</h3>
            </div>
        )
    }

    return (
        <div className="container">
            <h3>{user}</h3>
        </div>
    )

}

export default UseEffectMultiple
