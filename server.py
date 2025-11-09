import socket, threading

HOST = '0.0.0.0'
PORT = 12345
clients = []

def handle_client(conn, addr):
    print('Connected', addr)
    while True:
        try:
            msg = conn.recv(1024)
            if not msg: break
            for c in clients:
                if c != conn:
                    c.send(msg)
        except:
            break
    print('Disconnected', addr)
    clients.remove(conn)
    conn.close()

s = socket.socket()
s.bind((HOST, PORT))
s.listen()
print('Server listening', (HOST,PORT))

while True:
    conn, addr = s.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn,addr), daemon=True).start()
