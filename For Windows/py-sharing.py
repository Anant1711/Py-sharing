#-*- coding: utf-8 -*-

import os
import socket
import qrcode

#BANNER
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
print ("                                                                                      " + "By Anant" )
print ("")
print ("")
##############################################################################################################



PORT=9002                     #Port on which our server will run (YOU can change)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print ("="*100)
hostname = socket.gethostname()			#it will tell us hostname
print ("")
print ("--------------------------------------[" + hostname + "]------------------------------------")
print ("")

print ("------{Enter this IP into your reciever device's browser as [IP:9002] or Scan the share.png}-------")
print ("")

s.connect(("8.8.8.8", PORT))
print("-----------------------------------[" + s.getsockname()[0] + "]------------------------------------------")    #it will give us LAN IPv4
print ("")

img = qrcode.make(s.getsockname()[0]+":9002")				#for store data in qrcode png 
img.save("C:/Users/anako/OneDrive/Desktop/share.png")		#for saving qrcode png (change this path)

os.system("py -m http.server 9002")     	#it will start server at port 9002