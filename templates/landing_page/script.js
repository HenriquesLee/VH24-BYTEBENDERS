// Add click event listeners to role cards
const roleCards = document.querySelectorAll('.role-card');
let selectedRole = '';

roleCards.forEach(card => {
    card.addEventListener('click', () => {
        // Remove active class from all cards
        roleCards.forEach(c => c.classList.remove('active'));
        // Add active class to clicked card
        card.classList.add('active');
        // Set selected role based on data attribute
        selectedRole = card.getAttribute('data-value');
        console.log('Selected Role:', selectedRole); // You can use this value for further processing
    });
});

// Handle the proceed button click
document.querySelector('.submit-btn').addEventListener('click', () => {
    if (selectedRole) {
        alert(`You selected: ${selectedRole}`); // Replace with actual logic
    } else {
        alert('Please select a role before proceeding.');
    }
});
