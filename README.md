# GesturaSlide - Gesture-Based Presentation Control

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0096D6?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-36B7B7?style=for-the-badge&logoColor=white)](https://pyautogui.readthedocs.io/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

GesturaSlide is a Python application that enables gesture-based control of presentations using computer vision and machine learning. This project leverages MediaPipe and OpenCV to recognize hand gestures in real-time, allowing users to navigate slides, zoom, and move the cursor without touching any input devices. Featuring powerful real-time hand detection, intuitive gesture recognition, and smooth cursor control, GesturaSlide provides a hands-free presentation experience with minimal setup.

## Table of Contents

- [Key Features](#key-features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Usage Guide](#usage-guide)
- [Gesture Reference](#gesture-reference)
- [Technologies Used](#technologies-used)
- [Performance & Troubleshooting](#performance--troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Key Features

- **Real-Time Hand Detection**: Detects and tracks up to two hands simultaneously with high accuracy using MediaPipe's advanced machine learning models.
- **Intuitive Gesture Recognition**: Recognizes multiple hand gestures to control presentations—three fingers for next slide, two fingers for previous slide, and index finger for cursor movement.
- **Smooth Cursor Control**: Index finger tracking provides responsive mouse cursor movement with adaptive smoothing for natural interactions across any screen resolution.
- **Dual-Hand Zoom**: Control zoom levels with two hands—move hands apart to zoom in and bring them together to zoom out in any application.
- **Real-Time Feedback**: Visual feedback through hand landmark visualization helps users understand gesture detection in real-time during development and testing.
- **Easy Configuration**: Simple parameter adjustments in `main.py` allow customization of sensitivity, smoothing, and detection confidence for different environments and hardware.

---

## Getting Started

Follow these instructions to set up and run GesturaSlide on your local machine.

### Prerequisites

Make sure you have the following installed:
- **Python** (version 3.8 or higher)
- **pip** (Python Package Manager)
- **A functional webcam** or camera device connected to your system
- Minimum 4 GB RAM recommended for smooth real-time processing
- Modern processor (Intel i5 or equivalent) for optimal gesture detection

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/CodeMaster-D/GesturaSlide.git
   cd GesturaSlide
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   * On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   * On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   This will install all necessary packages including `mediapipe`, `opencv-python`, `numpy`, and `pyautogui`.

### Configuration

1. **Verify Webcam Connection**:
   - Ensure your webcam is properly connected and recognized by your system.
   - Test your webcam with your operating system's camera application to verify functionality.

2. **Adjust Application Parameters** (Optional):
   - Open `main.py` and modify the configuration section at the top:
     - `smooth_factor` (default: 7): Controls cursor smoothing. Higher values produce smoother movement.
     - `min_detection_confidence` (default: 0.7): Minimum confidence threshold for hand detection (0.0-1.0).
     - `min_tracking_confidence` (default: 0.7): Minimum confidence for tracking continuity.
     - `cooldown` (default: 0.8): Minimum time in seconds between slide navigation commands.
     - `cam_w` and `cam_h`: Input camera resolution settings.

3. **Optimize for Your Environment**:
   - In low-light conditions, decrease `min_detection_confidence` to 0.5-0.6.
   - In high-motion environments, increase `smoothing_factor` to 10-15.

### Running the Application

Start the application with the following command:

```bash
python main.py
```

Once running:
- Your webcam feed will open with real-time hand detection visualization.
- Perform gestures as described in the [Gesture Reference](#gesture-reference) section.
- Press **'q'** to exit the application safely.

---

## Project Structure

The project is organized for simplicity and clarity:

```
GesturaSlide/
├── main.py                       # Main application with gesture recognition logic
├── requirements.txt              # Project dependencies
├── README.md                     # Project documentation
├── CONTRIBUTING.md               # Contribution guidelines
├── CODE_OF_CONDUCT.md            # Community code of conduct
├── NOTICE                        # License notice and copyright
└── venv/                         # Virtual environment (created during setup)
```

---

## Usage Guide

### Prepare Your Environment

1. Ensure you have at least 2-3 feet of clear space in front of your webcam.
2. Position yourself in a well-lit area—natural or artificial lighting works equally well.
3. Avoid strong backlighting that might interfere with hand detection accuracy.
4. Start with the application running in front of your presentation software (PowerPoint, LibreOffice Impress, Google Slides, etc.).

### Hand Gestures

- **Navigate Forward**: Extend three fingers (thumb, index, middle) toward the camera to trigger the next slide.
- **Navigate Backward**: Extend two fingers (thumb and index/middle) to trigger the previous slide.
- **Move Cursor**: Raise only your index finger to move the mouse pointer naturally across the screen.
- **Pause Cursor**: Close your fist (all fingers folded) to pause cursor movement without pressing buttons.
- **Zoom In**: With both hands extended in front of the camera, move them apart to trigger zoom in.
- **Zoom Out**: Bring both hands closer together to trigger zoom out.

### Example Workflow

1. Open your presentation software and ensure it's in focus.
2. Run GesturaSlide.
3. Step back 2-3 feet from your webcam.
4. Use three-finger gestures to advance through slides.
5. Move your index finger to highlight specific areas on slides.
6. Use two-hand gestures to zoom into detailed content.
7. Press 'q' when finished to exit.

---

## Gesture Reference

| Gesture | Action | Use Case |
|---------|--------|----------|
| **3 Fingers Extended** | Next Slide | Move forward in presentation |
| **2 Fingers Extended** | Previous Slide | Return to previous slide |
| **Index Finger Only** | Mouse Cursor Control | Point and highlight areas |
| **All Fingers Closed (Fist)** | Cursor Pause | Temporary pause without clicks |
| **Both Hands Apart** | Zoom In | Magnify slide content |
| **Both Hands Together** | Zoom Out | Reduce zoom level |

---

## Core Features

GesturaSlide provides the following gesture-based functionalities:

* **Slide Navigation**: Three-finger gesture triggers the next slide (right arrow). Two-finger gesture triggers the previous slide (left arrow).
* **Cursor Control**: Index finger tracking provides smooth mouse cursor movement across the screen with adaptive coordinate mapping.
* **Zoom Functionality**: Two-hand zoom in by moving hands apart (Ctrl + =) and zoom out by bringing hands together (Ctrl + -).
* **Real-time Hand Detection**: Detects up to two hands simultaneously with configurable confidence thresholds for robust performance.
* **Smooth Finger Tracking**: Provides adaptive smoothing with configurable parameters for natural cursor movement.

## Technologies Used

GesturaSlide is built with modern computer vision and machine learning libraries:

* **Python**: Powerful and flexible programming language for rapid development.
* **MediaPipe**: Google's advanced machine learning framework providing pre-built hand detection and tracking solutions with state-of-the-art accuracy.
* **OpenCV (cv2)**: Industry-standard computer vision library handling video capture, image processing, and real-time frame analysis.
* **NumPy**: Efficient numerical computing library for mathematical operations on landmark coordinates and distance calculations.
* **PyAutoGUI**: Cross-platform library for programmatic control of mouse and keyboard at the system level.

---

## Performance & Troubleshooting

### Performance Optimization

- **Frame Rate**: Application runs at 30+ FPS on modern hardware. Monitor FPS in development mode.
- **CPU Usage**: Monitor CPU usage with system tools. Excessive usage may indicate detection sensitivity is too high.
- **Memory Usage**: Typically uses 200-400 MB RAM. If higher, restart the application.

### Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| Hand detection not working | Improve lighting, ensure hands are visible, check webcam isn't in use |
| Gestures registering inconsistently | Adjust `min_detection_confidence` and `min_tracking_confidence` values |
| Cursor movement too slow/fast | Modify `smooth_factor` parameter (lower = faster, higher = smoother) |
| Presentation not responding | Ensure presentation software window is active and in focus |
| Shaky cursor movement | Increase `smooth_factor` value for more stability |
| Zoom commands not working | Verify presentation software supports Ctrl += and Ctrl +- shortcuts |
| Low FPS or lag | Reduce camera resolution, check CPU load, close other applications |

### Environment-Specific Tips

- **Low-Light Environments**: Decrease `min_detection_confidence` to 0.5 and increase lighting.
- **High-Motion Environments**: Increase `smooth_factor` to 12-15 for stability.
- **Different Hardware**: Adjust `min_tracking_confidence` based on your processor speed.
- **Multiple Hands Detected**: Ensure at least 2 feet of space between people and camera.

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/ImproveGestureDetection`)
3. Commit your Changes (`git commit -m 'Add improved gesture detection'`)
4. Push to the Branch (`git push origin feature/ImproveGestureDetection`)
5. Open a Pull Request

For detailed contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md) and review our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

## License

This project is licensed under the **Apache License 2.0**—see the **[LICENSE](LICENSE)** file for the full terms and the **[NOTICE](NOTICE)** file for copyright and attribution details.

---

## Author

**Djob Misael**
- GitHub: [@CodeMaster-D](https://github.com/CodeMaster-D)
- Repository: [GesturaSlide](https://github.com/CodeMaster-D/GesturaSlide)

---

**Last Updated:** April 2026