#-*- coding: utf-8 -*-
import os
import socket
import pyqrcode

class bcolors:
    ENDC = '\033[95m'
    nm = '\033[93m'



print ("")
print ("")
print (" ███████████                                █████                           ███                     ")
print ("░░███░░░░░███                              ░░███                           ░░░                      ")
print (" ░███    ░███ █████ ████             █████  ░███████    ██████   ████████  ████  ████████    ███████")
print (" ░██████████ ░░███ ░███  ██████████ ███░░   ░███░░███  ░░░░░███ ░░███░░███░░███ ░░███░░███  ███░░███")
print (" ░███░░░░░░   ░███ ░███ ░░░░░░░░░░ ░░█████  ░███ ░███   ███████  ░███ ░░░  ░███  ░███ ░███ ░███ ░███")
print (" ░███         ░███ ░███             ░░░░███ ░███ ░███  ███░░███  ░███      ░███  ░███ ░███ ░███ ░███")
print (" █████        ░░███████             ██████  ████ █████░░████████ █████     █████ ████ █████░░███████")
print ("░░░░░          ░░░░░███            ░░░░░░  ░░░░ ░░░░░  ░░░░░░░░ ░░░░░     ░░░░░ ░░░░ ░░░░░  ░░░░░███")
print ("               ███ ░███                                                                     ███ ░███")
print ("              ░░██████                                                                     ░░██████ ")
print ("               ░░░░░░                                                                       ░░░░░░  ")
print ("                                                                                      " + bcolors.nm + "By Anant" + bcolors.ENDC)
print ("")
PORT=9004                     #Port on which our server will run (YOU can change)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print ("="*100)
hostname = socket.gethostname()                 #it will tell us hostname
print ("")
print ("--------------------------------------[" + hostname + "]------------------------------------")
print ("")

print ("------{Enter this IP into your receiver device's browser as [IP:9004] or Scan the share.png}-------")
print ("")

s.connect(("8.8.8.8", PORT))
print("-----------------------------------[" + s.getsockname()[0] + "]------------------------------------------")    #it will give us sender's IP
print ("")

img = pyqrcode.create(s.getsockname()[0]+":9004")                           #for store data in qrcode png 
img.png("/home/infinity/Desktop/share.png")           #for saving qrcode png (change this path)
print (img.terminal())
os.system("python3 -m http.server 9004")             #it will start server at port 9002
