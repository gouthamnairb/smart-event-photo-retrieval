// Global variables
let selfieFile = null;

// Preview the selfie before uploading
function previewSelfie(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    selfieFile = file;
    const preview = document.getElementById('selfie-preview');
    const reader = new FileReader();
    
    reader.onload = function(e) {
        preview.src = e.target.result;
        preview.classList.remove('hidden');
    };
    
    reader.readAsDataURL(file);
}

// Retrieve photos containing the uploaded selfie
async function retrievePhotos() {
    if (!selfieFile) {
        alert('Please upload a selfie first!');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', selfieFile);
    
    try {
        const response = await fetch('http://127.0.0.1:8000/upload_selfie', {
            method: 'POST',
            body: formData,
        });
        
        if (!response.ok) {
            throw new Error('Server returned ' + response.status);
        }
        
        const data = await response.json();
        console.log('Response data:', data);
        
        if (data.error) {
            alert(data.error);
            return;
        }
        
        displayPhotos(data.matching_photos);
    } catch (error) {
        console.error('Error retrieving photos:', error);
        alert('Error retrieving photos: ' + error.message);
    }
}

// Display the matching photos in the UI
function displayPhotos(photosList) {
    const container = document.getElementById('photo-container');
    container.innerHTML = '';
    
    if (!photosList || photosList.length === 0) {
        container.innerHTML = '<p>No matching photos found.</p>';
    } else {
        photosList.forEach(photoPath => {
            const img = document.createElement('img');
            // Use the correct URL format to fetch from the backend
            img.src = `http://127.0.0.1:8000/event_photos/${photoPath}`;
            img.alt = 'Event photo';
            img.onerror = function() {
                console.error(`Failed to load image: ${photoPath}`);
                this.src = 'data:image/svg+xml;charset=UTF-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22100%22%20height%3D%22100%22%3E%3Crect%20fill%3D%22%23ddd%22%20width%3D%22100%22%20height%3D%22100%22%2F%3E%3Ctext%20fill%3D%22%23666%22%20font-family%3D%22sans-serif%22%20font-size%3D%2210%22%20x%3D%2235%22%20y%3D%2255%22%3EError%3C%2Ftext%3E%3C%2Fsvg%3E';
            };
            container.appendChild(img);
        });
    }
    
    // Show the photos section
    document.getElementById('photos-section').classList.remove('hidden');
}

// Ensure the selfie-preview and photos-section are initially hidden
document.addEventListener('DOMContentLoaded', function() {
    const preview = document.getElementById('selfie-preview');
    if (preview) {
        preview.classList.add('hidden');
    }
    
    const photosSection = document.getElementById('photos-section');
    if (photosSection) {
        photosSection.classList.add('hidden');
    }
});