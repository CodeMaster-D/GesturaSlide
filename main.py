import cv2
import numpy as np
import pyautogui
import time
import mediapipe as mp

# --- CONFIG ---
pyautogui.PAUSE = 0
cam_w, cam_h = 640, 480
screen_w, screen_h = pyautogui.size()
smooth_factor = 7 
plocX, plocY = 0, 0
prev_time = 0
cooldown = 0.8
is_fist = False
dist_start = None

# --- INISIALISASI MEDIAPIPE (VERSI AMAN) ---
# Menggunakan struktur standar yang seharusnya ada di 0.10.9
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2, 
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

def count_fingers(lm):
    fingers = []
    # Logika Jempol (Sumbu X)
    if lm[4].x > lm[3].x: fingers.append(1)
    else: fingers.append(0)
    
    # 4 Jari (Sumbu Y) - Landmark Tip < Landmark Pip
    tips = [8, 12, 16, 20]
    for tip in tips:
        if lm[tip].y < lm[tip-2].y: fingers.append(1)
        else: fingers.append(0)
    return fingers

print("Sistem GesturaSlide Aktif! Tekan 'q' untuk berhenti.")

while cap.isOpened():
    success, img = cap.read()
    if not success: break
    
    img = cv2.flip(img, 1)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_img)
    curr_time = time.time()

    if results.multi_hand_landmarks:
        # 1. LOGIKA ZOOM (Dua Tangan)
        if len(results.multi_hand_landmarks) == 2:
            h1 = results.multi_hand_landmarks[0].landmark[0]
            h2 = results.multi_hand_landmarks[1].landmark[0]
            dist_now = np.hypot(h1.x - h2.x, h1.y - h2.y)
            
            if dist_start is None: 
                dist_start = dist_now
            else:
                if dist_now - dist_start > 0.15: # Menjauh
                    pyautogui.hotkey('ctrl', '=')
                    dist_start = dist_now
                elif dist_start - dist_now > 0.15: # Mendekat
                    pyautogui.hotkey('ctrl', '-')
                    dist_start = dist_now
        
        # 2. LOGIKA NAVIGASI (Satu Tangan)
        else:
            dist_start = None
            lm = results.multi_hand_landmarks[0].landmark
            fingers = count_fingers(lm)
            total_fingers = sum(fingers)

            # --- MOUSE MOVEMENT (Hanya jika tidak mengepal) ---
            if total_fingers > 0:
                # Mengambil koordinat ujung jari telunjuk (Landmark 8)
                fx = np.interp(lm[8].x * cam_w, [100, 540], [0, screen_w])
                fy = np.interp(lm[8].y * cam_h, [100, 380], [0, screen_h])
                
                curr_x = plocX + (fx - plocX) / smooth_factor
                curr_y = plocY + (fy - plocY) / smooth_factor
                
                pyautogui.moveTo(curr_x, curr_y)
                plocX, plocY = curr_x, curr_y

            # --- NAVIGASI SLIDE ---
            if curr_time - prev_time > cooldown:
                if total_fingers == 3: # Tiga jari = Next
                    pyautogui.press('right')
                    prev_time = curr_time
                elif total_fingers == 2: # Dua jari = Prev
                    pyautogui.press('left')
                    prev_time = curr_time

            # --- LOGIKA SELEKSI (Mengepal = Slide Sorter) ---
            if total_fingers == 0:
                if not is_fist:
                    pyautogui.press('g') # Shortcut PowerPoint
                    is_fist = True
            else:
                if is_fist and total_fingers >= 4:
                    time.sleep(0.3) 
                    pyautogui.press('enter')
                    is_fist = False

        # Gambar visualisasi tangan di layar
        for hand_lms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)
    else:
        dist_start = None

    cv2.imshow("GesturaSlide PKL - Preview", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()