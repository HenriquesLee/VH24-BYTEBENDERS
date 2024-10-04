// campaign-script.js
document.addEventListener("DOMContentLoaded", () => {
    const addCampaignBtn = document.getElementById("add-section");
    const popupForm = document.getElementById("popupForm");
    const closeBtn = document.getElementById("closeBtn");
    const requestForm = document.getElementById("requestForm");

    // Show the popup form when the button is clicked
    addCampaignBtn.addEventListener("click", () => {
        popupForm.style.display = "block";
    });

    // Close the popup form when the close button is clicked
    closeBtn.addEventListener("click", () => {
        popupForm.style.display = "none";
    });

    // Close the popup form when clicking outside of the modal
    window.addEventListener("click", (event) => {
        if (event.target == popupForm) {
            popupForm.style.display = "none";
        }
    });

    // Handle form submission
    requestForm.addEventListener("submit", (event) => {
        event.preventDefault(); // Prevent page reload
        // You can add logic here to handle the form data, like sending it to a server
        alert("Request sent!");
        popupForm.style.display = "none"; // Close the form after submission
        requestForm.reset(); // Reset the form fields
    });
});
