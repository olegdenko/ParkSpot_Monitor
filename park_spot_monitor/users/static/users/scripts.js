document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.custom-button');

    buttons.forEach(button => {
        button.addEventListener('mousedown', function() {
            this.style.backgroundColor = '#0056b3';
        });

        button.addEventListener('mouseup', function() {
            this.style.backgroundColor = '#007BFF';
        });
    });
});
