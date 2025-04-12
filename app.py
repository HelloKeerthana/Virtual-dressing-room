from flask import Flask, render_template, Response, request
from camera import generate_frames
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/camera')
def camera():
    shirt = request.args.get('shirt', None)
    return render_template('camera.html', shirt=shirt)

@app.route('/video_feed')
def video_feed():
    shirt = request.args.get('shirt', None)
    return Response(generate_frames(shirt), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/wardrobe')
def wardrobe():
    
    wardrobe_path = os.path.join(app.root_path, 'static', 'wardrobe')
    
    
    items = [f for f in os.listdir(wardrobe_path) 
            if f.lower().endswith('.png')]
    
    
    items.sort(key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))
    
    return render_template('wardrobe.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
