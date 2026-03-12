import socket
HOST = '127.0.0.1'  
PORT = 8080    
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print("Server running on http://127.0.0.1:8080")
while True:
    client_socket, addr = server_socket.accept()
    print("Connected by", addr)
    request = client_socket.recv(1024).decode()
    print("Request:\n", request)
    if "GET" in request:
        with open("index.html", "r") as file:
            content = file.read()
        response = "HTTP/1.1 200 OK\n"
        response += "Content-Type: text/html\n\n"
        response += content
        client_socket.send(response.encode())
    elif "POST" in request:
        data = request.split("\r\n\r\n")[1]
        with open("uploaded.html", "w") as file:
            file.write(data)
        response = "HTTP/1.1 200 OK\n\nFile Uploaded Successfully"
        client_socket.send(response.encode())
    client_socket.close()