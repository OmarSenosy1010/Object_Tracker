# Object Tracker with OpenCV

This project provides a simple yet powerful object tracking tool using OpenCV's CSRT tracker. It allows you to select an object in a video stream (from webcam or file) and track its movement in real-time.

## Features
- Real-time object tracking using the CSRT algorithm
- Supports webcam and video file input
- Interactive object selection with bounding box
- Visual feedback: tracking box and status display
- Easy to use and extend

## Requirements
- Python 3.6+
- OpenCV (cv2)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Object_Tracker.git
   cd Object_Tracker
   ```
2. **Install dependencies:**
   ```bash
   pip install opencv-python
   # For advanced tracking features, you may need:
   # pip install opencv-contrib-python
   ```

## Usage
1. **Run the script:**
   ```bash
   python track.py
   ```
2. **Select the object:**
   - When the first frame appears, use your mouse to draw a bounding box around the object you want to track.
   - Press ENTER or SPACE to confirm selection.
3. **Tracking:**
   - The script will track the selected object in real-time.
   - Press `q` to quit.

### Using a Video File
- To track an object in a video file, edit `track.py`:
  - Comment out the webcam line:
    ```python
    # cap = cv2.VideoCapture(0)
    ```
  - Uncomment and set your video file path:
    ```python
    cap = cv2.VideoCapture("your_video.mp4")
    ```

## Troubleshooting
- **Cannot read from the camera or video file:**
  - Ensure your webcam is connected or the video file path is correct.
  - Check that your camera is not being used by another application.
- **OpenCV errors:**
  - Make sure you have installed the correct version of OpenCV (`opencv-python`).
  - For advanced tracking features, `opencv-contrib-python` may be required:
    ```bash
    pip install opencv-contrib-python
    ```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- Built with [OpenCV](https://opencv.org/)
- CSRT tracker from OpenCV's tracking module 