import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.43.107"

# create new socket for client which only accepts IPV4 addresses
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect with the server socket
client.connect((SERVER,PORT))

def send(msg):
     # encode message string to byte format
     message = msg.encode(FORMAT)
     # get message length
     msg_len = len(message)
     # cast length of the message to be sent to string and encode to byte format
     send_len = str(msg_len).encode(FORMAT)
     # add 64 - send_len no of padding in byte format to send_len (because server expect 64 bytes)
     send_len += b' ' * (HEADER - len(send_len))
     # send message length and message to server
     client.send(send_len)
     client.send(message)
     print(client.recv(HEADER).decode(FORMAT))


send("Hello from client!")
send("how are you doing?")
send(DISCONNECT_MESSAGE)     
