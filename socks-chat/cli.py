import socket

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as serve:
    serve.connect((socket.gethostbyname(socket.gethostname()),8080))
    
    while True:
        print("1. Log In!")
        print("2. Sign UP!")
        choice = input()

        if choice == "1":
            serve.send(b"LOGIN")
            serve.send(input("Enter Username:").encode())
            serve.send(input("Enter Password:").encode())
            print(serve.recv(1000).decode())
        
        if choice == "2":
            serve.send(b"SIGNUP")
            serve.send(input("Enter Username:").encode())
            serve.send(input("Enter Password:").encode())
            print(serve.recv(1000).decode())
        else:
            print("Wrong Input")