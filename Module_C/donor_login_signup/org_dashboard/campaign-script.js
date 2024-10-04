// Get elements
const addButton = document.querySelector('.add-btn');
const popupForm = document.getElementById('popupForm');
const closePopup = document.querySelector('.close-popup');

// Show the popup when the add button is clicked
addButton.addEventListener('click', () => {
    popupForm.style.display = 'flex';
});

// Close the popup when the close button is clicked
closePopup.addEventListener('click', () => {
    popupForm.style.display = 'none';
});

// Close the popup when clicking outside of it
window.addEventListener('click', (event) => {
    if (event.target === popupForm) {
        popupForm.style.display = 'none';
    }
});

// Handle form submission
const requestForm = document.getElementById('request-form');
requestForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent form submission
    alert('Request sent!'); // Show a success message (you can replace this with actual functionality)
    popupForm.style.display = 'none'; // Close the popup
    requestForm.reset(); // Reset form fields
});
