import cv2
import socket
import numpy as np

# Create a VideoCapture object and open the default camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error opening camera.")
    exit()

# Create a socket to connect to the remote machine
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('<remote_machine_ip_address>', <port>))

# Read the frames from the camera and send them to the remote machine
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Break the loop if the frame is not read successfully
    if not ret:
        break

    # Encode the frame as a JPEG image and send it to the remote machine
    encoded_frame = cv2.imencode('.jpg', frame)[1].tobytes()
    client_socket.sendall(encoded_frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
cap.release()

# Close the socket and all windows
client_socket.close()
cv2.destroyAllWindows()
