import socket
import threading

username = input("Choose a username: ")
host_ip = '127.0.0.1'
port = 52525

user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    user.connect((host_ip, port))
except ConnectionRefusedError:
    print("Error: Connection refused. Make sure the server is running.")
    exit()

def receive():
    while True:
        try:
            message = user.recv(1024).decode('ascii')
            if message == 'NICK':
                user.send(username.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            user.close()
            break

def write():
    while True:
        message = input('')
        user.send(message.encode('ascii'))
        if message == '/quit':
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()