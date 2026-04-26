document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('fileInput');
    const uploadArea = document.getElementById('upload-label');

    // Handle Image Preview
    fileInput.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                // Background change karke preview dikhana
                uploadArea.innerHTML = `
                    <img src="${e.target.result}" class="mx-auto h-48 w-48 object-cover rounded-xl mb-2 border-2 border-green-500">
                    <p class="text-green-400 font-medium">${file.name}</p>
                    <p class="text-xs text-gray-500">Click to change photo</p>
                `;
            }
            reader.readAsDataURL(file);
        }
    });

    // Drag and Drop Effects (Optional)
    ['dragenter', 'dragover'].forEach(eventName => {
        uploadArea.addEventListener(eventName, () => {
            uploadArea.classList.add('border-green-500');
        }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, () => {
            uploadArea.classList.remove('border-green-500');
        }, false);
    });
});