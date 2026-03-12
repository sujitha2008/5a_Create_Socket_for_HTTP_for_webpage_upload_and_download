import socket
HOST = '127.0.0.1'
PORT = 8080
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
choice = input("Enter 1 to Download page, 2 to Upload page: ")
if choice == "1":
    request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    client_socket.send(request.encode())
    response = client_socket.recv(4096).decode()
    print("Server Response:\n")
    print(response)
elif choice == "2":
    data = "<html><body><h2>Uploaded Page</h2></body></html>"
    request = "POST / HTTP/1.1\r\n"
    request += "Host: localhost\r\n"
    request += "Content-Length: " + str(len(data)) + "\r\n\r\n"
    request += data
    client_socket.send(request.encode())
    response = client_socket.recv(4096).decode()
    print("Server Response:\n", response)
client_socket.close()
