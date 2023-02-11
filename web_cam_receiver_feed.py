import cv2
import socket
import numpy as np

# Create a socket to receive the video feed from the remote machine
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', <port>))
server_socket.listen(1)

connection, address = server_socket.accept()

# Read the frames from the socket and display them using OpenCV
while True:
    # Receive the encoded frame from the remote machine
    encoded_frame = b''
    while True:
        data = connection.recv(4096)
        encoded_frame += data
        if len(data) < 4096:
            break

    # Decode the encoded frame and display it using OpenCV
    frame = cv2.imdecode(np.frombuffer(encoded_frame, np.uint8), cv2.IMREAD_COLOR)
    cv2.imshow("Remote Video Feed", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
connection.close()
server_socket.close()
cv2.destroyAllWindows()
