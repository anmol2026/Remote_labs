import socket, cv2, pickle, struct
from django.http import HttpResponse
from django.shortcuts import render
# from .models import *
from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

@gzip.gzip_page
def Home(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'app1.html')

#to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
# create socket
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host_ip = '192.168.53.132'
# port = 9999
# client_socket.connect((host_ip, port))
# data = b""
# payload_size = struct.calcsize("Q")
# while True:
#     while len(data) < payload_size:
#         packet = client_socket.recv(4 * 1024)
#         if not packet: break
#         data += packet
#     packed_msg_size = data[:payload_size]
#     data = data[payload_size:]
#     msg_size = struct.unpack("Q", packed_msg_size)[0]
#
#     while len(data) < msg_size:
#         data += client_socket.recv(4 * 1024)
#     frame_data = data[:msg_size]
#     data = data[msg_size:]
#     frame = pickle.loads(frame_data)
#     frame = cv2.flip(frame, 1)
#     cv2.imshow("RECEIVING VIDEO", frame)
#     key = cv2.waitKey(1) & 0xFF
#     if key == ord('q'):
#         break
# client_socket.close()