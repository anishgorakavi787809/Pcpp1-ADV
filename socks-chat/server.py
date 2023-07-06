import socket

print(socket.gethostbyname(socket.gethostname()))

account_table = {}

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as serve:
    serve.bind((socket.gethostbyname(socket.gethostname()),8080))
    serve.listen()

    while True:
        conn,ip = serve.accept()
        with conn:
            while True:
                d = conn.recv(1000).decode()
                print(d)
                match d:
                    case "LOGIN":
                        uname = conn.recv(255).decode()
                        pword = conn.recv(255).decode()
                        if account_table.get(uname) == pword:
                            conn.send(f"Hello, {uname}. You are logged in\n".encode())
                        else:
                            conn.send(b"Wrong username/Wrong password")
                    case "SIGNUP":
                        uname = conn.recv(255).decode()
                        pword = conn.recv(255).decode()
                        if account_table.get(uname):
                            conn.send(b"Error:Username exists")
                        else:
                            account_table[uname] = pword
                            conn.send(b"Signed you up!")