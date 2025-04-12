import cv2
import mediapipe as mp
import numpy as np
import os

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

def overlay_shirt(frame, shirt_img, x_offset, y_offset):
    h, w = shirt_img.shape[:2]
    bg_h, bg_w = frame.shape[:2]

    x1, y1 = max(x_offset, 0), max(y_offset, 0)
    x2, y2 = min(x_offset + w, bg_w), min(y_offset + h, bg_h)

    sx1, sy1 = max(0, -x_offset), max(0, -y_offset)
    sx2, sy2 = sx1 + (x2 - x1), sy1 + (y2 - y1)

    shirt_crop = shirt_img[sy1:sy2, sx1:sx2]

    if shirt_crop.shape[2] == 4:
        alpha = shirt_crop[:, :, 3:] / 255.0
        shirt_rgb = shirt_crop[:, :, :3]
    else:
        alpha = np.ones_like(shirt_crop[:, :, :1], dtype=np.float32)
        shirt_rgb = shirt_crop

    frame[y1:y2, x1:x2] = (1 - alpha) * frame[y1:y2, x1:x2] + alpha * shirt_rgb
    return frame

def generate_frames(shirt_filename="shirt1.png"):
    cap = cv2.VideoCapture(0)

    # Load shirt image
    shirt_path = os.path.join(os.path.dirname(__file__), 'static', 'wardrobe', shirt_filename)
    shirt_img = cv2.imread(shirt_path, cv2.IMREAD_UNCHANGED)
    if shirt_img is None:
        print("Shirt image not found.")
        return

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)

        if results.pose_landmarks:
            lm = results.pose_landmarks.landmark
            h, w = frame.shape[:2]
            l_sh = lm[mp_pose.PoseLandmark.LEFT_SHOULDER]
            r_sh = lm[mp_pose.PoseLandmark.RIGHT_SHOULDER]

            x1, y1 = int(l_sh.x * w), int(l_sh.y * h)
            x2, y2 = int(r_sh.x * w), int(r_sh.y * h)

            shoulder_dist = abs(x2 - x1)
            shirt_w = int(shoulder_dist * 1.8)
            shirt_h = int(shirt_w * shirt_img.shape[0] / shirt_img.shape[1])

            center_x = (x1 + x2) // 2
            x_offset = center_x - shirt_w // 2
            y_offset = max(y1, y2) - 68  # Lowered to avoid face overlap

            resized_shirt = cv2.resize(shirt_img, (shirt_w, shirt_h))
            frame = overlay_shirt(frame, resized_shirt, x_offset, y_offset)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()
