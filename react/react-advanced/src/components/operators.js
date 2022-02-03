import React, { useEffect, useState } from 'react'

const Operators = () => {
    const [show, setShow] = useState(false)

    return (
        <>
            <div className="container">
                {show && <Item />}
                {/* {show || <Item />} */}
                {/* {show? <Item /> : <h3>Value is False</h3>} */}
                <button className="btn" onClick={() => setShow(!show)}>Show/Hide</button>
            </div>
        </>
    )
}

const Item = () => {
    const [size, setSize] = useState(window.innerWidth)

    const checkSize = () => {
        setSize(window.innerWidth)
    }

    useEffect(() => {
        //on resize updating size variable 
        window.addEventListener('resize', checkSize)

        //clean of eventlistner from dom if component is removed/hide
        return () => {
            window.removeEventListener('resize', checkSize)
        }
    })

    return (
        <>
            <h3>Window Size</h3>
            <h4>{size} Px</h4>
        </>
    )
}
export default Operators
