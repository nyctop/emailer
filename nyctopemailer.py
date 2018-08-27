import os
import subprocess
import sys
subprocess.run("clear", shell=True)

print("""
   ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████  ▄█   ▄█          ▄████████    ▄████████ 
  ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███  ███         ███    ███   ███    ███ 
  ███    █▀  ███   ███   ███   ███    ███ ███▌ ███         ███    █▀    ███    ███ 
 ▄███▄▄▄     ███   ███   ███   ███    ███ ███▌ ███        ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀███▀▀▀     ███   ███   ███ ▀███████████ ███▌ ███       ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███    █▄  ███   ███   ███   ███    ███ ███  ███         ███    █▄  ▀███████████ 
  ███    ███ ███   ███   ███   ███    ███ ███  ███▌    ▄   ███    ███   ███    ███ 
  ██████████  ▀█   ███   █▀    ███    █▀  █▀   █████▄▄██   ██████████   ███    ███ 
                                               ▀                        ███    ███

                    Emailer by Nycto - Version 1.0                 
""")



# sendemail -t (destination address ) –f (from eg. foo@bar.com ) –s (server:port) –xu (smtp server username ) –xp (smtp password) –m (message)

print(" Type your SMTP SERVER DETAILS :")

server = input("Server Adress :  ")
#serverport = input("Server Port :  ")
serverusername = input("Server Username : ")
serverpass = input("Server Password : ")
print("Type Email DETAILS: ")
reciver = input("Reciver Adress(to) : ")
sender = input("Sender Adress(from) : ")


message = input("MESSAGE :    ")
subprocess.call("sendemail" + " -t " + reciver + " -f " + sender +  "-s " + " -xu " + serverusername + " -xp " + serverpass + " -m " + message, shell=True)
