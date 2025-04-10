# Overview

This Program is a simple chat, between clients. Just start the messaging.py to start the server and then all clients can run user.py and set their username and they can then chat between one another.

I have never messed with networking stuff and wanted to do something simple to play around with it and settled on this idea I had for a chat room.

[Software Demo Video](https://youtu.be/mFsjT5j_zBg)

# Network Communication

This can be done just straight in your Command line. and will connect users that are on the same network

This uses TCP and is sent through the port 52525

The format of the messages being sent between the client and server in this chat application is primarily plain text encoded in ASCII.

# Development Environment

I used VS code to set up the python, and then Command Prompt from Windows to run the server and clients.

I used python to code the server and clients, using the Socket and Threading Libraries.

# Useful Websites

* [Wikipedia - Client-Server Model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
* [How-To Geek](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)

# Future Work

* Private messaging by like using /msg <username> <message>.
* Rich text formatting so adding bold and italics and underlines.
* Notifications like a desktop sound for new messages.