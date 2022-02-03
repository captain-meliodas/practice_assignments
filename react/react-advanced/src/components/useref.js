import React, { useRef, useEffect } from 'react'

const UseRefBasics = () => {
    //useRef can't call re-render
    const refInput = useRef(null)
    const refContainer = useRef(null)

    const handleSubmit = (ev) => {
        ev.preventDefault()
        console.log(refInput.current.value)
        console.log(refContainer.current)
    }

    useEffect(() => {
        refInput.current.focus();
    })

    return (
        <>
            <form className="form" onSubmit={handleSubmit}>
                <div>
                    <input
                        type="text"
                        ref={refInput}
                    />
                    <button type="submit"> Submit </button>
                </div>
                <div ref={refContainer}>refcontainer</div>
            </form>

        </>
    )
}

export default UseRefBasics
