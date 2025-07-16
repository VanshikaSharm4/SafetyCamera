from flask import Flask, render_template, jsonify, request
import subprocess
import os
import signal
import psutil
import time
import cv2

app = Flask(__name__)

# Global variable to store the camera process
camera_process = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

def find_available_camera():
    """Find the first available camera device"""
    for i in range(10):  # Check first 10 camera indices
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cap.release()
                return i
        cap.release()
    return 0  # Default to 0 if no camera found

@app.route('/api/start_camera', methods=['POST'])
def start_camera():
    global camera_process
    
    try:
        # Check if camera is already running
        if camera_process and camera_process.poll() is None:
            return jsonify({'success': False, 'message': 'Camera is already running'})
        
        # Find available camera
        camera_index = find_available_camera()
        
        # Start the camera process (app.py) with the correct camera index
        camera_process = subprocess.Popen(['python', 'app.py', '--device', str(camera_index)], 
                                        stdout=subprocess.PIPE, 
                                        stderr=subprocess.PIPE)
        
        # Wait a moment to see if it starts successfully
        time.sleep(3)
        
        if camera_process.poll() is None:
            return jsonify({'success': True, 'message': f'Camera started successfully on device {camera_index}'})
        else:
            # Get error output if process failed
            stdout, stderr = camera_process.communicate()
            error_msg = stderr.decode() if stderr else "Unknown error"
            return jsonify({'success': False, 'message': f'Failed to start camera: {error_msg}'})
            
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error starting camera: {str(e)}'})

@app.route('/api/stop_camera', methods=['POST'])
def stop_camera():
    global camera_process
    
    try:
        if camera_process and camera_process.poll() is None:
            # Terminate the camera process
            camera_process.terminate()
            
            # Wait for it to terminate gracefully
            try:
                camera_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                # Force kill if it doesn't terminate gracefully
                camera_process.kill()
                camera_process.wait()
            
            camera_process = None
            return jsonify({'success': True, 'message': 'Camera stopped successfully'})
        else:
            return jsonify({'success': False, 'message': 'Camera is not running'})
            
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error stopping camera: {str(e)}'})

@app.route('/api/camera_status', methods=['GET'])
def camera_status():
    global camera_process
    
    if camera_process and camera_process.poll() is None:
        return jsonify({'running': True, 'pid': camera_process.pid})
    else:
        return jsonify({'running': False, 'pid': None})

@app.route('/api/test_camera', methods=['GET'])
def test_camera():
    """Test if any camera is available"""
    try:
        camera_index = find_available_camera()
        if camera_index >= 0:
            return jsonify({'success': True, 'message': f'Camera found at index {camera_index}'})
        else:
            return jsonify({'success': False, 'message': 'No camera found'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'Error testing camera: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 