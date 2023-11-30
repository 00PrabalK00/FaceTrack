# FaceTrack
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <h1>Face Detection and Servo Control</h1>
</head>

<body>
        <img src="/Images/ezgif-5-33003841ff.gif" >
    <p>This project combines face detection using OpenCV in Python and servo control with Arduino to create a simple
        interactive system. The Python code captures webcam frames, detects faces, calculates forehead coordinates, and
        sends the data to the Arduino through serial communication. The Arduino code receives the data and controls two
        servo motors to track the detected face.</p>
         <img src="/Images/image_2023-11-30_231031386.png" alt="Face Detection" width="300" height="200">
    <h2>Getting Started</h2>
    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.x</li>
        <li>OpenCV for Python</li>
        <li>Arduino IDE</li>
        <li>Servo library (for Arduino servo control)</li>
    </ul>
    <h3>Installation</h3>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/your-username/face-detection-servo-control.git</code></pre>
        <li>Install the required Python packages:</li>
        <pre><code>pip install opencv-python </code></pre>
    </ol>
    <h2>Usage</h2>
    <ol>
        <li>Upload the Arduino code (<code>face_detection_servo_control.ino</code>) to your Arduino board using the
            Arduino IDE.</li>
        <li>Connect your Arduino board to the computer.</li>
        <li>Run the Python script (<code>face_detection_python.py</code>) to start the face detection and servo
            control system:</li>
        <pre><code>python face_detection_python.py</code></pre>
        <p>Adjust the serial port (<code>'COM4'</code>) in the Python script based on your Arduino connection.</p>
        <li>Press 'q' to exit the Python script.</li>
    </ol>
    <h2>Configuration</h2>
    <ul>
        <li>Modify the Arduino code if you change the pins used for servo control.</li>
        <li>Adjust Python script parameters for webcam resolution, serial port, and face detection settings.</li>
    </ul>
    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
    <h2>Acknowledgments</h2>
    <ul>
        <li>Face detection using OpenCV: <a href="https://opencv.org/">OpenCV</a></li>
        <li>Servo control with Arduino: <a href="https://www.arduino.cc/">Arduino</a></li>
    </ul>

</body>

</html>


