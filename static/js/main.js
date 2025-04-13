// Main JavaScript for PhotoFind Application

document.addEventListener('DOMContentLoaded', function() {
  // DOM Elements
  const dropzone = document.getElementById('dropzone');
  const fileInput = document.getElementById('file-upload');
  const previewImage = document.getElementById('preview-image');
  const uploadPrompt = document.querySelector('.upload-prompt');
  const uploadPreview = document.querySelector('.upload-preview');
  const clearUploadBtn = document.getElementById('clear-upload');
  const findPhotosBtn = document.getElementById('find-photos-btn');
  const resultsSection = document.getElementById('results-section');
  const photoGrid = document.getElementById('photo-grid');
  const photoCount = document.getElementById('photo-count');
  const loadingIndicator = document.getElementById('loading-indicator');
  const noResults = document.getElementById('no-results');
  
  // File upload handling
  let selectedFile = null;
  
  // Handle file selection
  fileInput.addEventListener('change', handleFileSelect);
  
  // Handle drag and drop
  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, preventDefaults, false);
  });
  
  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }
  
  ['dragenter', 'dragover'].forEach(eventName => {
    dropzone.addEventListener(eventName, highlight, false);
  });
  
  ['dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, unhighlight, false);
  });
  
  function highlight() {
    dropzone.classList.add('active');
  }
  
  function unhighlight() {
    dropzone.classList.remove('active');
  }
  
  dropzone.addEventListener('drop', handleDrop, false);
  
  function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;
    
    if (files.length) {
      fileInput.files = files;
      handleFileSelect({ target: { files: files } });
    }
  }
  
  // Click on dropzone to trigger file input
  uploadPrompt.addEventListener('click', function() {
    fileInput.click();
  });
  
  // Clear upload button
  clearUploadBtn.addEventListener('click', function(e) {
    e.stopPropagation();
    clearFileUpload();
  });
  
  // Find photos button
  findPhotosBtn.addEventListener('click', findMatchingPhotos);
  
  // Handle file selection
  function handleFileSelect(e) {
    const files = e.target.files;
    
    if (!files.length) return;
    
    selectedFile = files[0];
    
    // Check if file is an image
    if (!selectedFile.type.match('image.*')) {
      showMessage('Please select an image file (JPEG, PNG).', 'error');
      clearFileUpload();
      return;
    }
    
    // Display preview
    const reader = new FileReader();
    
    reader.onload = function(e) {
      previewImage.src = e.target.result;
      uploadPrompt.classList.add('hidden');
      uploadPreview.classList.remove('hidden');
      findPhotosBtn.disabled = false;
    };
    
    reader.readAsDataURL(selectedFile);
  }
  
  // Clear file upload
  function clearFileUpload() {
    fileInput.value = '';
    selectedFile = null;
    previewImage.src = '#';
    uploadPrompt.classList.remove('hidden');
    uploadPreview.classList.add('hidden');
    findPhotosBtn.disabled = true;
  }
  
  // Show message toast
  function showMessage(message, type = 'info') {
    // Remove any existing message
    const existingMessage = document.querySelector('.message-toast');
    if (existingMessage) {
      existingMessage.remove();
    }
    
    // Create message element
    const messageEl = document.createElement('div');
    messageEl.className = `message-toast ${type}`;
    messageEl.textContent = message;
    
    // Add to DOM
    document.body.appendChild(messageEl);
    
    // Show the message
    setTimeout(() => {
      messageEl.classList.add('show');
    }, 10);
    
    // Hide after delay
    setTimeout(() => {
      messageEl.classList.remove('show');
      setTimeout(() => {
        messageEl.remove();
      }, 300);
    }, 3000);
  }
  
  // Find matching photos
  function findMatchingPhotos() {
    if (!selectedFile) return;
    
    // Show results section and loading indicator
    resultsSection.classList.remove('hidden');
    loadingIndicator.classList.remove('hidden');
    photoGrid.innerHTML = '';
    noResults.classList.add('hidden');
    
    // Create form data
    const formData = new FormData();
    formData.append('file', selectedFile);
    
    // Send request to server
    fetch('/upload_selfie', {
      method: 'POST',
      body: formData
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Server error: ' + response.status);
      }
      return response.json();
    })
    .then(data => {
      // Hide loading indicator
      loadingIndicator.classList.add('hidden');
      
      // Process results
      if (data.error) {
        // Show error
        showError(data.error);
        return;
      }
      
      const matchingPhotos = data.matching_photos || [];
      
      if (matchingPhotos.length === 0) {
        // No results found
        noResults.classList.remove('hidden');
        photoCount.textContent = '0';
      } else {
        // Display matching photos
        displayMatchingPhotos(matchingPhotos);
        photoCount.textContent = matchingPhotos.length;
        
        // Show success message
        const message = matchingPhotos.length === 1 
          ? '1 matching photo found!' 
          : `${matchingPhotos.length} matching photos found!`;
        showMessage(message, 'success');
      }
    })
    .catch(error => {
      console.error('Error:', error);
      loadingIndicator.classList.add('hidden');
      showError('An error occurred while processing your request.');
    });
  }
  
  // Display matching photos
  function displayMatchingPhotos(photos) {
    photoGrid.innerHTML = '';
    
    photos.forEach(photo => {
      const photoCard = document.createElement('div');
      photoCard.className = 'photo-card';
      
      const img = document.createElement('img');
      img.src = `/event_photos/${photo}`;
      img.alt = 'Event Photo';
      img.loading = 'lazy';
      
      // Add download capability
      photoCard.addEventListener('click', function() {
        const link = document.createElement('a');
        link.href = img.src;
        link.download = photo.split('/').pop();
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      });
      
      // Add tooltip
      const tooltip = document.createElement('div');
      tooltip.className = 'tooltip';
      tooltip.textContent = 'Click to download';
      photoCard.appendChild(tooltip);
      
      // Handle image loading errors
      img.onerror = function() {
        photoCard.innerHTML = '<div class="error-placeholder">Image not available</div>';
      };
      
      photoCard.appendChild(img);
      photoGrid.appendChild(photoCard);
    });
  }
  
  // Show error in the results section
  function showError(message) {
    noResults.querySelector('h4').textContent = 'Error';
    noResults.querySelector('p').textContent = message;
    noResults.classList.remove('hidden');
    photoCount.textContent = '0';
    showMessage(message, 'error');
  }

  // Check for mobile devices and adjust the layout if needed
  function checkMobile() {
    if (window.innerWidth <= 900) {
      // For mobile, ensure the results section is below
      resultsSection.style.display = 'none';
      findPhotosBtn.addEventListener('click', function() {
        resultsSection.style.display = 'block';
        setTimeout(() => {
          resultsSection.scrollIntoView({ behavior: 'smooth' });
        }, 100);
      });
    }
  }

  // Call on load
  checkMobile();

  // Also call on resize
  window.addEventListener('resize', checkMobile);
}); 