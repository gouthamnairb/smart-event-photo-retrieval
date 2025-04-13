# PhotoFind - Smart Event Photo Retrieval

PhotoFind is an intelligent web application that helps users find photos of themselves from event photo collections using facial recognition technology. Upload a selfie, and the AI will identify all event photos containing you.

## Features

- **AI-Powered Face Recognition**: Uses DeepFace library to match facial features with high accuracy
- **Simple User Interface**: Clean, intuitive interface focused on functionality
- **Drag-and-Drop Upload**: Easy photo upload with drag-and-drop functionality
- **Real-time Feedback**: Immediate visual feedback during processing
- **Responsive Design**: Works on both desktop and mobile devices
- **One-Click Downloads**: Download matched photos with a single click
- **Visual Notifications**: Toast messages for operation status

## Tech Stack

- **Backend**: Flask web framework with Python
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Face Recognition**: DeepFace library
- **Image Processing**: OpenCV and PIL
- **Styling**: Custom CSS with responsive design

## Project Structure

```
/
├── app.py                  # Main Flask application
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── services/               # Core services
│   ├── face_recognition.py # Face recognition logic
│   └── file_storage.py     # File handling utilities
├── static/                 # Static assets
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript files
│   └── images/             # Icons and images
├── templates/              # HTML templates
│   └── index.html          # Main application page
├── event_photos/           # Directory for event photos
└── user_uploads/           # Directory for user uploads
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/gouthamnairb/smart-event-photo-retrieval.git
   cd photofind
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create required directories**
   ```bash
   mkdir -p event_photos user_uploads
   ```

5. **Add event photos**
   
   Place your event photos in the `event_photos` directory. Supported formats are:
   - JPG/JPEG
   - PNG

### Running the Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Access the application**
   
   Open a web browser and navigate to:
   ```
   http://localhost:8000
   ```

## Usage Guide

1. **Upload a Selfie**
   - Click "Choose a file" or drag and drop a photo into the upload area
   - A preview of your selfie will appear

2. **Find Matching Photos**
   - Click the "Find My Photos" button
   - Wait for the AI to process your selfie and find matches

3. **View and Download Results**
   - Matching photos will appear in the results section
   - Click on any photo to download it

## Troubleshooting

- **No faces detected**: Ensure your selfie has a clear, well-lit face
- **No matching photos**: Try a different selfie or adjust lighting conditions
- **Slow performance**: Large photo collections may take longer to process

## Development

### Local Development

1. Enable debug mode in `config.py`:
   ```python
   DEBUG = True
   ```

2. Run the application:
   ```bash
   python app.py
   ```

### Customization

- Edit `static/css/main.css` to customize the styling
- Modify `templates/index.html` to change the layout
- Update `static/js/main.js` to adjust behavior

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- DeepFace library for facial recognition
- Flask framework for web application development
- OpenCV for image processing capabilities

## Contact

For questions or support, please open an issue on the repository. 
