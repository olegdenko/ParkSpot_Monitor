document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('uploadForm');
    var loader = document.getElementById('loader');

    form.addEventListener('submit', handleFormSubmit);

    function handleFormSubmit(event) {
        event.preventDefault();

        var fileInput = document.getElementById('image');
        if (fileInput.files.length === 0) {
            showError('Please select an image file to upload.');
            return;
        }

        var formData = new FormData(this);
        showLoader();

        sendFormData(formData)
            .then(handleRecognitionResult)
            .catch(handleError)
            .finally(hideLoader);
    }

    function sendFormData(formData) {
        return fetch('/upload/', {
            method: 'POST',
            body: formData
        })
        .then(handleResponse);
    }

    function handleResponse(response) {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Network response was not ok.');
        }
    }

    function handleRecognitionResult(data) {
        if (data.plate_number) {
            showSuccess(`Recognized plate number: ${data.plate_number}`);
        } else {
            showError('License plate recognition failed.');
        }
    }

    function handleError(error) {
        showError('Error occurred. Try again later.');
        console.error(error);
    }

    function showLoader() {
        loader.style.display = 'block';
    }

    function hideLoader() {
        loader.style.display = 'none';
    }

    function showError(message) {
        alert(message);
    }

    function showSuccess(message) {
        alert(message);
    }
});
