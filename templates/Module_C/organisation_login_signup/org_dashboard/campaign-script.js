// Get the modal
const popupForm = document.getElementById("popupForm");

// Get the button that opens the modal
const addBtn = document.querySelector(".add-btn");

// Get the <span> element that closes the modal
const closeBtn = document.querySelector(".close-popup");

// When the user clicks on the button, open the modal
addBtn.onclick = function () {
    popupForm.style.display = "flex"; // Change to flex to center the popup
};

// When the user clicks on <span> (x), close the modal
closeBtn.onclick = function () {
    popupForm.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == popupForm) {
        popupForm.style.display = "none";
    }
};

// Prevent default form submission
document.getElementById("request-form").onsubmit = function (event) {
    event.preventDefault();
    // Add your form submission logic here
    console.log("Form submitted!");
    popupForm.style.display = "none"; // Close the popup after submission
};
