function clearForm() {
    document.getElementById("registrationForm").reset();
}

function validateForm() {
    var userId = document.getElementById("userId").value;
    var name = document.getElementById("name").value;
    var address = document.getElementById("address").value;
    var mobileNo = document.getElementById("mobileNo").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;

    if (!userId || !name || !address || !mobileNo || !email || !password || !confirmPassword) {
        alert("All fields are required");
        return false;
    }

    if (isNaN(mobileNo) || mobileNo.length !== 10) {
        alert("Please enter a valid 10-digit mobile number");
        return false;
    }

    // Basic email validation
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("Please enter a valid email address");
        return false;
    }

    // Password and Confirm Password match
    if (password !== confirmPassword) {
        alert("Password and Confirm Password do not match");
        return false;
    }

    return true;
}
