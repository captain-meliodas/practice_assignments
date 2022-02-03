import React, { useState } from 'react'

const UseStateCounter = () => {
    const [counter, setCounter] = useState(0)
    const reset = () => {
        setCounter(0)
    }
    const setCounterCallback = () => {
        // setTimeout doesn't fetch previous state it only fetch curren state if callback is not set
        //when clicked multiple times before 2000 milliseconds
        // setTimeout(()=>{
        //     setCounter(counter+1)
        // },2000)

        //setting callback to fetch previous state when clicked multiple times before 2 sec
        setTimeout(() => {
            setCounter((prevState) => {
                return prevState + 1
            })
        }, 2000)
    }
    return (
        <div className="container">
            <h1>Use state Counter example</h1>
            <h3>{counter}</h3>
            <button className="btn" onClick={() => setCounter(counter + 1)}>Increase</button>
            <button className="btn" onClick={() => reset()}>Reset</button>
            <button className="btn" onClick={() => setCounter(counter - 1)}>Decrease</button>
            <button className="btn" onClick={() => setCounterCallback()}>Complex Increase</button>
        </div>
    )

}

export default UseStateCounter