import socket 
import threading

# fixed sized header of 64 bytes
HEADER = 64
PORT = 5050
# get ip address of the devices server is running
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

print(f"ip: {SERVER}")


# create new socket for server which only accepts IPV4 addresses
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the ip address and port to the socket
server.bind((SERVER, PORT))

def handle_client(sock, addr):
     print(f"[NEW CONNECTION] {addr} connected")
     
     connected = True
     
     while connected:
          # decode message length from byte format to string using utf-8
          msg_len = sock.recv(HEADER).decode(FORMAT)
          
          # get upcoming message length
          if msg_len:
               msg_len = int(msg_len)

               # decode receiving message from byte format to string using utf-8
               msg = sock.recv(msg_len).decode(FORMAT)
          
               # if client sends disconnect message close the connection with the client
               if msg == DISCONNECT_MESSAGE:
                    connected = False

               print(f"[INCOMING MESSAGE] '{addr}' message: {msg}")
               
               # send a message back to client
               sock.send("message received".encode(FORMAT))
               
     # close the connection
     sock.close()


# start server
def start():
     # set server socket to listening state
     server.listen()
     print(f"[LISTENING] server is listening on port {SERVER}")
     while True:
          # accept incoming connections from clients
          sock, addr = server.accept()
          # create new thread for each client
          thread = threading.Thread(target=handle_client, args=(sock, addr))
          thread.start()
          # no of active client connections
          print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1} active connections...")


print(f"[STARTING] server is starting at port {PORT}...")
start()







