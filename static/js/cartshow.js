document.addEventListener('DOMContentLoaded', function () {
    displayCartItems();
})

function displayCartItems() {
    let cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    let cartList = document.getElementById('cart-items');
    let totalQuantity = 0;
    let Price=0;
    console.log(cartItems)
    if (cartItems.length === 0) {
        cartList.innerHTML = '<p>THE CART IS EMPTY</p>';

    } else {
        cartList.innerHTML = '';
        cartItems.forEach(function (item) {
            // let listItem = document.createElement('li');
            let listItem = document.createElement('div');

            listItem.innerHTML = `
            <div style="display: flex; align-items: center; margin-bottom: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); height:4rem;">
            <img src="${item.product_img}" alt="food-image" style="width: 50px; height: 50px; border-radius:50%; margin-left:2rem" >
            <span><${item.title}</span>
            <span style="margin-left: 6rem; margin-right: 6rem;">Rs.${item.product_price}</span>
            <a href="" onclick="decrementItem('${item.title}')" style="margin-right: 6rem; text-decoration:none; font-size: 2rem; padding: 0.2rem;">-</a>
            <span style="margin-right: 6rem;">${item.quantity}</span>
            <a href="" onclick="incrementItem('${item.title}')" style="text-decoration:none; font-size: 1.7rem;">+</a>
            </div>
            `;
            cartList.appendChild(listItem);

            totalQuantity += item.quantity;
            Price+=item.product_price*item.quantity;

        });
        // let rightSection = document.querySelector('.right');
        // rightSection.querySelector('h3:nth-child(1)').textContent = `Items: ${totalQuantity}`;
        let itemsCountElement = document.querySelector('.right h3:nth-child(1)');
        // itemsCountElement.textContent = `Items: ${totalQuantity}`;
        // if (totalQuantity === 0) {
        //     itemsCountElement.textContent = `Items: 0`;
        // }
        if (totalQuantity === 0) {
            itemsCountElement.textContent = `Items: 0`; 
        } else {
            itemsCountElement.textContent = `Items: ${totalQuantity}`; 
        }
 
        let itemsCountElement2 = document.querySelector('.right h3:nth-child(2)');
        itemsCountElement2.textContent = `Price: ₹ ${Price}`; 
        let itemsCountElement4 = document.querySelector('.right h3:nth-child(4)');
        itemsCountElement4.textContent = `Total Price: ₹ ${Price +49}`; 
        
        document.getElementById('total-price-input').value = Price+49;
    }
}


function incrementItem(title) {
    let cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    cartItems.forEach(function (item) {
        if (item.title === title) {
            item.quantity++;
        }
    });
    localStorage.setItem('cart', JSON.stringify(cartItems));
    displayCartItems();
}

function decrementItem(title) {
    let cartItems = JSON.parse(localStorage.getItem('cart')) || [];
    for (let i = 0; i < cartItems.length; i++) {
        if (cartItems[i].title === title) {
            if (cartItems[i].quantity > 1) {
                cartItems[i].quantity--;
            } else {
                cartItems.splice(i, 1);
            }
            break;
        }
    }
    localStorage.setItem('cart', JSON.stringify(cartItems));
    displayCartItems();
}

function goCart(){
    let valid_address=document.getElementById('useraddress')
    let valid_mail=document.getElementById('inputEmail')
    let valid_mobile=document.getElementById('inputMobile')
    let valid_pin=document.getElementById('inputPin')
    console.log("hhhbh")

    let dataToSend=localStorage.getItem('cart')
    let y=document.getElementById('cart_dataid')
    y.value=dataToSend
    console.log("a")
    console.log(dataToSend)
    console.log("aa")

}

// function total() {
//     var sum = 0;
//     let cart = JSON.parse(localStorage.getItem('cart')) || [];
//     cart.forEach((item) => {
//         sum += item.price;
//     })
// }