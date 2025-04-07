document.addEventListener('DOMContentLoaded', function () {
    let container = document.getElementById('container');
    let alertBox = document.getElementById('custom-alert');

    // Handle sign-in/sign-up toggle
    if (container) {
        window.toggle = function () { // Making toggle accessible globally
            container.classList.toggle('sign-in');
            container.classList.toggle('sign-up');
        };

        setTimeout(() => {
            container.classList.add('sign-in');
        }, 200);
    } else {
        console.error('Container element not found!');
    }

    // Auto dismiss alert after 3 seconds
    if (alertBox) {
        setTimeout(() => dismissAlert(), 3000);
    }
});

// Function to dismiss the alert
function dismissAlert() {
    let alertBox = document.getElementById('custom-alert');
    if (alertBox) {
        alertBox.classList.add('hidden'); // Slide up and fade out
        setTimeout(() => alertBox.remove(), 500);
    }
}