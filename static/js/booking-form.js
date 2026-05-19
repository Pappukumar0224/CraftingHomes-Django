

// function validateForm() {
//     var name = document.getElementById('name').value;
//     var email = document.getElementById('email').value;
//     var pincode = document.getElementById('pincode').value;
//     var address = document.getElementById('address').value;
//     var description = document.getElementById('description').value;
//     var phone = document.getElementById('phone').value;
//     var bookingDate = document.getElementById('bookingDate').value;
//     var scheduleDate = document.getElementById('scheduleDate').value;

//     if (name == "" || email == "" || pincode == "" || address == "" || description == "" || phone == "" || bookingDate == "" || scheduleDate == "") {
//         alert("All fields must be filled out");
//         return false;
//     }
//     if (!validateEmail(email)) {
//         alert("Invalid email format");
//         return false;
//     }
//     if (!validatePhone(phone)) {
//         alert("Invalid phone number format");
//         return false;
//     }
//     return true;
// }

// function validateEmail(email) {
//     var re = /\S+@\S+\.\S+/;
//     return re.test(email);
// }

// function validatePhone(phone) {
//     var re = /^\d{10}$/;
//     return re.test(phone);
// }

// function showConfirmation() {
//     alert("Thank you for booking! We will contact you shortly.");
// }

// document.getElementById('closeButton').addEventListener('click', function() {
//     document.getElementById('popupForm').style.display = 'none';
// });

// document.getElementById('popupForm').addEventListener('submit', function(event) {
//     event.preventDefault();
//     if (validateForm()) {
//         showConfirmation();
//         document.getElementById('popupForm').style.display = 'none';
//         this.submit();
//     }
// });

// // booking-form.js
// document.getElementById('bookNowButton').addEventListener('click', function(event) {
//     // Check if the user is logged in
//     if (userIsLoggedIn()) {
//         // User is logged in, open the booking form
//         window.location.href = 'form.html';
//     } else {
//         // User is not logged in, redirect to the login page
//         window.location.href = 'login.html';
//     }
// });

// function userIsLoggedIn() {
//     // Check if the user is logged in
//     // For demonstration purposes, return true if the user is logged in
//     return true;
// }

document.getElementById('bookNowButton').addEventListener('click', function(event) {
    // Check if the user is logged in
    if (userIsLoggedIn()) {
        // User is logged in, open the booking form
        window.location.href = 'login.html';  //dot' change
    } else {
        // User is not logged in, redirect to the login page
        window.location.href = 'login.html';
    }
});

function userIsLoggedIn() {
    // Check if the user is logged in
    // For demonstration purposes, return true if the user is logged in
    return true;
}
