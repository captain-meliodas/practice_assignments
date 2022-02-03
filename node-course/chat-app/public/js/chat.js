const socket = io()

// socket.on('countUpdated', (count) => {
//     console.log('The count has been updated!', count)
// })

// document.querySelector('#increment').addEventListener('click', () => {
//     console.log('Clicked')
//     socket.emit('increment')
// })

const $messageForm = document.querySelector('#welcome_form')
const $messageFormButton = document.querySelector('#welcome_form button')
const message = document.querySelector('#welcome_form #message')
const $sendLocationButton = document.querySelector('#send_location button')

const messageTemplate = document.querySelector("#message-template").innerHTML
const $messages_div = document.querySelector("#messages_div")

const locationTemplate = document.querySelector("#location-message-template").innerHTML
const sideBarTemplate = document.querySelector("#sideBarTemplate").innerHTML
const $sideBarDiv = document.querySelector("#sideBar")

//QS library for parsing query string 
const { username, room } = Qs.parse(location.search, { ignoreQueryPrefix: true })

const autoscroll = () => {
    if ($messages_div.scrollHeight - $messages_div.clientHeight != $messages_div.scrollTop) {
        $messages_div.scrollTop = $messages_div.scrollHeight
    }
    //New message element
    // const $newMessage = $messages_div.lastElementChild

    // //height of the new message
    // const newMessageStyles = getComputedStyle($newMessage)
    // const newMessageMargin = parseInt(newMessageStyles.marginBottom)
    // const newMessageHeight = $newMessage.offsetHeight + newMessageMargin

    // //visible height
    // const visibleHeight = $messages_div.offsetHeight

    // //height of message container
    // const containerHeight = $messages_div.scrollHeight

    // //scroll bottom
    // const scrollOffset = $messages_div.scrollTop + visibleHeight

    // console.log($messages_div.scrollHeight - $messages_div.scrollTop, $messages_div.clientHeight, "---------------------")
    // console.log($messages_div.scrollHeight, $messages_div.scrollTop)

    // if ($messages_div.scrollHeight - $messages_div.scrollTop >= $messages_div.clientHeight) {
    //     //you are at the bottom of the scroll
    // }
    // if ($messages_div.scrollHeight - $messages_div.scrollTop !== $messages_div.clientHeight) {
    //     userhasscrolled = true
    // }
    // if (!userhasscrolled) {

    //     $messages_div.scrollTop = $messages_div.scrollHeight
    // }
}

//---------------------------------------------
$messageForm.addEventListener('submit', (ev) => {
    ev.preventDefault()
    $messageFormButton.setAttribute('disabled', 'disabled')

    socket.emit('emit_from_client', message.value, (error) => {
        $messageFormButton.removeAttribute('disabled')
        message.value = ''
        message.focus()
        if (error) {
            return console.log(error)
        }
        console.log("Message has been delivered")
    })
})

socket.on('emit_from_server', (message) => {
    const html = Mustache.render(messageTemplate, {
        message: message.text,
        createdAt: moment(message.createdAt).format('hh:mm a'),
        username: message.username
    })
    $messages_div.insertAdjacentHTML("beforeend", html)
    autoscroll()
})
//---------------------------------------------


//---------------------------------------------
$sendLocationButton.addEventListener('click', (ev) => {
    if (!navigator.geolocation) {
        return alert("Browser does not support gelocation")
    }
    $sendLocationButton.setAttribute('disabled', 'disabled')
    navigator.geolocation.getCurrentPosition((position) => {
        socket.emit('sendLocation', {
            latitude: position.coords.latitude,
            longitude: position.coords.longitude
        }, () => {
            $sendLocationButton.removeAttribute('disabled')
        })
    })
})
socket.on('clientLocation', (response) => {
    const html = Mustache.render(locationTemplate, {
        href: response.text,
        createdAt: moment(response.createdAt).format('hh:mm a'),
        username: response.username
    })
    $messages_div.insertAdjacentHTML("beforeend", html)
    autoscroll()
})
//-------------------------------------------------------------

//emits when user is joined 
socket.emit('join', { username, room }, (error) => {
    if (error) {
        alert(error)
        location.href = "/"
    }
})

//userlist in room
socket.on('roomData', ({ room, users }) => {
    const html = Mustache.render(sideBarTemplate, {
        room,
        users
    })
    $sideBarDiv.innerHTML = html
})