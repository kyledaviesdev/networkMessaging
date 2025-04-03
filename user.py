import socket
import threading

username = input("Chose a username: ")

user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user.connect(('127.0.0.1', 52525))

def receive():
    while True:
        try:
            message = user.recv(1024).decode('ascii')
            if message == 'NICK':
                user.send(username.encode('ascii'))
            else:
                print(message)
        except:
            print("An issue occurred!")
            user.close()
            break

def write():
    while True:
        message = f'{username}: {input("")}'
        user.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
