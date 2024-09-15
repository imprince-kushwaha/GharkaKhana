window.onload = function() {
    updateCartCount(); // Update cart count when the page loads
};
function addToCart(productTitle, product_id,product_img,product_price) {
    // console.log(product_id)
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    console.log(cart)
    let found=0;
    if (cart) {

        cart.forEach((item) => {
            if (item.product_id === product_id) {
                item.quantity += 1;
                found=1;
            }
            
        })
        if(!found){
            let product = { title: productTitle, quantity: 1, product_id: product_id,product_img:product_img,product_price:product_price };
            // console.log(product_price)
            cart.push(product);
        }
        localStorage.setItem('cart', JSON.stringify(cart));

        updateCartCount();
    }
}

// function updateCartCount() {
//     let cartCount = document.getElementById('cart-icon');
//     let cart = JSON.parse(localStorage.getItem('cart')) || [];
//     let count=0;
//     console.log(cart);
//     if(cart){
//         cart.forEach((item)=>{
//             count+=item.quantity;
//         })
//     }
//     if (cart.length > 0) {
//         cartCount.textContent = `${cart.length}`;
//     } else {
//         cartCount.textContent = " ";
//     }
// }
function updateCartCount() {
    let cartCount = document.getElementById('cart-plus'); // Assuming 'cart-plus' is the ID of the <a> tag
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let totalCount = 0;

    if (cart && cart.length > 0) {
        cart.forEach((item) => {
            totalCount += item.quantity;
        });
        cartCount.textContent = `${totalCount}`;
    } else {
        cartCount.textContent = "0"; // Set default count to 0 if cart is empty
    }
}



// function viewCart(){
//     let cart=JSON.parse(localStorage.getItem('cart'))||[];
//     if(cart.length>0){
//         window.location.href='cartshow.html';
//     }else{
//         alert('Your Cart is Empty');
//     }
// }



function handleCartClick(event) {
    event.preventDefault(); // Prevent default navigation action

    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    if (cart.length > 0) {
        // If cart is not empty, allow navigation to checkout page
        window.location.href = event.target.getAttribute('href');
    } else {
        // If cart is empty, show alert and do not navigate
        alert('Your Cart is Empty');
    }
}

