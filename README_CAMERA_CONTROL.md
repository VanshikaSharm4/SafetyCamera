# SafetyCam Camera Control System

This system allows you to start and stop the camera (app.py) from the admin web interface.

## Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Flask Web Server**
   ```bash
   python flask_app.py
   ```

3. **Access the Admin Panel**
   - Open your web browser
   - Go to: `http://localhost:5000/admin`
   - You'll see the admin panel with camera controls

## How to Use

### Starting the Camera
1. In the admin panel, locate the "Live Camera Access" section
2. Click the "Start Camera" button
3. The system will start the `app.py` process which opens the camera
4. The status indicator will show "Camera Online" with a green dot

### Stopping the Camera
1. Click the "Stop Camera" button
2. The system will terminate the `app.py` process
3. The status indicator will show "Camera Offline" with a red dot

### Features
- **Real-time Status**: The system automatically checks camera status every 5 seconds
- **Visual Indicators**: Green dot for online, red dot for offline
- **Error Handling**: Proper error messages if camera start/stop fails
- **Process Management**: Safely terminates camera processes

## Technical Details

- **Flask App**: `flask_app.py` serves the web interface
- **Camera Process**: `app.py` handles the actual camera operations
- **API Endpoints**:
  - `POST /api/start_camera` - Starts the camera
  - `POST /api/stop_camera` - Stops the camera
  - `GET /api/camera_status` - Checks camera status

## Troubleshooting

1. **Camera won't start**: Check if another instance is running
2. **Permission errors**: Ensure camera access permissions
3. **Port conflicts**: Change port in `flask_app.py` if needed

## File Structure
```
SafetyCam/
├── flask_app.py          # Flask web server
├── app.py               # Camera application
├── templates/
│   └── admin.html       # Admin page template
├── static/
│   ├── css/
│   │   └── style.css    # Styling
│   └── js/
│       └── admin.js     # Admin page JavaScript
└── requirements.txt     # Python dependencies
``` 