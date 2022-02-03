//asynchronous callbacks
setTimeout(() => {
    console.log("-------------------------")
},2000)

//mimicing the asyncronous callbacks
const add = (a,b,callback) => {
    setTimeout(() => {
        let sum = a+b
        callback(sum) //callback returning the value (here return will not work in asynchronous calls)
    },2000)
}

add(1,4, (sum) =>{
    console.log(sum)
})