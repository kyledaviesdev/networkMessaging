import threading
import socket

host = '127.0.0.1' #localhost
port = 52525
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

users = []
usernames = []

def anouncement(message):
    for user in users:
        user.send(message)

def handle(user):
    while True:
        try:
            message = user.recv(1024)
            anouncement(message)
        except:
            index = users.index(user)
            users.remove(user)
            user.close()
            username = usernames[index]
            anouncement(f'{username} left...'.encode('ascii'))
            usernames.remove(username)
            break

def receive():
    while True:
        user, address = server.accept()
        print(f'Connected with {str(address)}')
        user.send('NICK'.encode(ascii))
        username = user.recv(1024).decode('ascii')
        usernames.append(username)
        users.append(user)

        print(f'Your username is {username}!')
        anouncement(f'{username} joined!'.encode('ascii'))
        user.send("You've connected to the server!".encode('ascii'))

        thread = threading.Thread(target=handle, args=(user,))
        thread.start()

print("Server is live!")
receive()