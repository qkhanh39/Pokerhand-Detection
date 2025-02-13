from ultralytics import YOLO
import cv2
from PokerHandFunction import PokerHandDetection
import math
import streamlit as st

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    
    

    model = YOLO("src/CardDetection.pt").to('cuda')

    classNames = ['10C', '10D', '10H', '10S', 
            '2C', '2D', '2H', '2S', 
            '3C', '3D', '3H', '3S', 
            '4C', '4D', '4H', '4S', 
            '5C', '5D', '5H', '5S', 
            '6C', '6D', '6H', '6S', 
            '7C', '7D', '7H', '7S', 
            '8C', '8D', '8H', '8S', 
            '9C', '9D', '9H', '9S', 
            'AC', 'AD', 'AH', 'AS', 
            'JC', 'JD', 'JH', 'JS', 
            'KC', 'KD', 'KH', 'KS', 
            'QC', 'QD', 'QH', 'QS']

    st.title("Real-time Pokerhand Detection")
    framePlaceholder = st.empty()
    stopButtonPressed = st.button("Stop")

    while cap.isOpened() and not stopButtonPressed:
        success, img = cap.read()
        if not success:
            st.write("The video capture has ended")
            break
        
        # img = cv2.flip(img, 1)
        results = model(img, stream=True, device='cuda')
        hand = []
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])
                cv2.putText(img, f'{classNames[cls]} {conf}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
                if conf > 0.8:
                    hand.append(classNames[cls])
        hand = list(set(hand))  


        if (len(hand)) == 5:
            pokerHandName = PokerHandDetection(hand)
            text = f'Your hand {pokerHandName}'
            cv2.putText(img, text, (150, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        framePlaceholder.image(img, channels="RGB")
        
        if cv2.waitKey(1) & 0xFF == ord("q") or stopButtonPressed:
            break   
        
        
        # cv2.imshow("Image", img)
        # cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()
