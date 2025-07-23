import cv2

# this for webcam 
cap = cv2.VideoCapture(0)
# if u want to use a video file, uncomment the next line
# cap = cv2.VideoCapture("your_video.mp4")

# to read a video and get the first frame
ret, frame = cap.read()
if not ret:
    print("cannot read from the camera or video file")
    cap.release()
    exit()

# to select the object to track using a bounding box
bbox = cv2.selectROI("select", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("select")

# tracker function using CSRT
tracker = cv2.TrackerCSRT_create()
tracker.init(frame, bbox)

# Main loop: Continuously read frames, update the tracker, draw results, and handle user input
while True:
    ret, frame = cap.read()
    if not ret:
        break
    success, bbox = tracker.update(frame)
    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Tracking", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Lost", (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    cv2.imshow("Object Tracker", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
