const location_form = document.querySelector("form")
console.log(location_form)
location_form.addEventListener('submit', (ev) => {
    ev.preventDefault()
    let query = document.querySelector("#location_input")
    fetch(`http://127.0.0.1:3000/weather?address=${query.value}`).then((response) => {
        // console.log(response.json())
        response.json().then((data) => {
            if (data.error) {
                console.log(data.error)
            } else {
                console.log(data);
            }
        })
    })
})