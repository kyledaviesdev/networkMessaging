import threading
import socket

host = '127.0.0.1' #localhost
port = 52525
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

users = []
usernames = {}  # Use a dictionary to map user objects to usernames

def broadcast(message):
    for user in users:
        try:
            user.send(message)
        except:
            # Handle potential disconnection during broadcast
            remove_user(user)

def remove_user(user):
    if user in users:
        index = users.index(user)
        users.remove(user)
        if user in usernames:
            username = usernames[user]
            broadcast(f'Server: {username} disconnected.'.encode('ascii'))
            del usernames[user]

def handle(user):
    while True:
        try:
            message = user.recv(1024)
            # Check for command
            if message.startswith(b'/'):
                if message.startswith(b'/nick '):
                    new_nickname = message[6:].decode('ascii').strip()
                    if user in usernames:
                        old_nickname = usernames[user]
                        if new_nickname and new_nickname not in usernames.values():
                            usernames[user] = new_nickname
                            broadcast(f'Server: {old_nickname} changed their nickname to {new_nickname}'.encode('ascii'))
                            user.send(f'Server: Your nickname has been changed to {new_nickname}'.encode('ascii'))
                        else:
                            user.send('Server: Invalid or already taken nickname.'.encode('ascii'))
                    else:
                        user.send('Server: You need to set a nickname first.'.encode('ascii'))
                elif message.startswith(b'/help'):
                    user.send(b'Server: Available commands: /nick <new_nickname>, /list, /quit')
                elif message.startswith(b'/list'):
                    user_list = ', '.join(usernames.values())
                    user.send(f'Server: Current users: {user_list}'.encode('ascii'))
                elif message.startswith(b'/quit'):
                    remove_user(user)
                    user.close()
                    break
                else:
                    user.send(b'Server: Unknown command. Type /help for available commands.')
            else:
                if user in usernames:
                    username = usernames[user]
                    broadcast(f'{username}: {message.decode("ascii")}'.encode('ascii'))
                else:
                    user.send(b'Server: Please set a nickname before sending messages.')
        except:
            remove_user(user)
            user.close()
            break

def receive():
    while True:
        user, address = server.accept()
        print(f'Connected with {str(address)}')
        user.send('NICK'.encode('ascii'))
        nickname = user.recv(1024).decode('ascii').strip()
        if nickname and nickname not in usernames.values():
            usernames[user] = nickname
            users.append(user)
            print(f'Nickname of the user is {nickname}!')
            broadcast(f'Server: {nickname} joined the chat!'.encode('ascii'))
            user.send("Server: You've connected to the server! Type /help for commands.".encode('ascii'))
            thread = threading.Thread(target=handle, args=(user,))
            thread.start()
        else:
            user.send('Server: Nickname already taken or invalid. Disconnecting.'.encode('ascii'))
            user.close()

print("Server is live!")
receive()