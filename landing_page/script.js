window.onload = function() {
    const form = document.querySelector('form');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const role = document.querySelector('input[name="role"]:checked').value;
        alert(`You signed up as a ${role}`);
    });
};
