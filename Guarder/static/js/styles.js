document.addEventListener('DOMContentLoaded', function() {
    let container = document.getElementById('container');

    if (container) {
        toggle = () => {
            container.classList.toggle('sign-in');
            container.classList.toggle('sign-up');
        }

        setTimeout(() => {
            container.classList.add('sign-in');
        }, 200);
    } else {
        console.error('Container element not found!');
    }
});
