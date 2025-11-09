import socket, threading

HOST = '127.0.0.1'
PORT = 12345

s = socket.socket()
s.connect((HOST,PORT))

def recv():
    while True:
        try:
            data = s.recv(1024)
            if not data: break
            print("\n" + data.decode())
        except:
            break

threading.Thread(target=recv, daemon=True).start()

try:
    while True:
        msg = input()
        if not msg: continue
        s.send(msg.encode())
except KeyboardInterrupt:
    s.close()
