// Get references to the add button and popup
const addBtn = document.querySelector('.add-btn');
const popup = document.querySelector('.popup');
const closePopup = document.querySelector('.close-popup');

// Show the popup when the add button is clicked
addBtn.addEventListener('click', () => {
    popup.style.display = 'block';
});

// Hide the popup when the close button is clicked
closePopup.addEventListener('click', () => {
    popup.style.display = 'none';
});

// Optional: Hide the popup when clicking outside of it
window.addEventListener('click', (event) => {
    if (event.target === popup) {
        popup.style.display = 'none';
    }
});
