// Handle popup open and close functionality
document.addEventListener('DOMContentLoaded', function () {
    const addSection = document.getElementById('add-section');
    const popupForm = document.getElementById('popupForm');
    const closePopup = document.querySelector('.close-popup');
  
    // Open popup when Add Button is clicked
    addSection.addEventListener('click', function () {
      popupForm.style.display = 'block';
    });
  
    // Close popup when close button is clicked
    closePopup.addEventListener('click', function () {
      popupForm.style.display = 'none';
    });
  
    // Close popup when clicking outside the popup content
    window.addEventListener('click', function (event) {
      if (event.target === popupForm) {
        popupForm.style.display = 'none';
      }
    });
  });
  