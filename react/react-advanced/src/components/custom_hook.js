import { useState, useEffect, useCallback } from 'react'

export const useFetch = (url) => {
    const [loading, setLoading] = useState(true)
    const [data, setData] = useState([])

    //re-create the function only when url changes
    const fetchUrl = useCallback(async () => {
        const response = await fetch(url)
        const users = await response.json()
        setData(users)
        setLoading(false)
    }, [url])

    useEffect(() => {
        fetchUrl()
    }, [url])

    return { loading, data }
}
