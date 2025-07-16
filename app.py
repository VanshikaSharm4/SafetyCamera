# app.py
# from weapon_detection import WeaponDetector
from flask import Flask, render_template, request, Response, url_for
from model import SafetyCam
import threading
import cv2
import time

app = Flask(__name__)

# Keep a reference to the running detection thread
active_cam = None

def gen_frames():
    global active_cam
    print("🟡 gen_frames started")
    while active_cam and active_cam.running:
        frame = getattr(active_cam, 'latest_frame', None)
        if frame is not None:
            try:
                ret, buffer = cv2.imencode('.jpg', frame)
                if not ret:
                    print("❌ Frame encoding failed")
                    continue
                frame = buffer.tobytes()
                print("✅ Frame encoded and sending to browser")
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                print(f"❌ Exception in gen_frames: {e}")
        else:
            print("⚠️ No frame available yet")
            time.sleep(0.03)
            
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/', methods=['GET', 'POST'])
def index():
    global active_cam

    show_feed = False
    if request.method == 'POST':
        camera_url = request.form.get('camera_url')
        if camera_url == '0' or camera_url.strip() == '':
            camera_url = 0
        show_feed = request.form.get('show_feed') == 'on'

        if active_cam is not None:
            active_cam.stop()

        # Start detection with new parameters
        active_cam = SafetyCam(camera_url, show_feed)
        threading.Thread(target=active_cam.start).start()

        return render_template('index.html', message='Detection Started.', show_feed=show_feed)

    return render_template('index.html', show_feed=show_feed)

@app.route('/stop', methods=['GET', 'POST'])
def stop():
    global active_cam
    if active_cam is not None:
        active_cam.stop()
        active_cam = None
    return render_template('index.html', message='Detection Stopped.')

if __name__ == '__main__':
    app.run(debug=True)