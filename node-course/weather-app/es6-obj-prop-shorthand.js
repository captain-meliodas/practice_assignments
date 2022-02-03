const product = {
    label:"ES6 Object Shorthand Property",
    price: 500,
    stock: 2211,
    salePrice: undefined
}

//destructuring object
const {label,price} = product
console.log(label,price);

//renaming variable name while destructuring
const {label:renamedLabel,price:costprice} = product
console.log(renamedLabel,costprice, "-----renamed labels");

const saledproduct = {
    product:"Saled Product",
    salePrice: 499,
    stock: 2211,
}
const transaction = (type,{product,salePrice}) => {
    console.log(type)
    console.log(product)
    console.log(salePrice)
}

transaction('debit',saledproduct)