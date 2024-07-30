import socket 
import threading

clients=[] 

def handle_client(client_socket, addr):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"received from {addr}:{message}")
                broadcast(message,client_socket)
            else:
                break
        except:
            clients.remove(client_socket)
            break
    client_socket.close()


def broadcast(message, client_socket):
    for client in clients:
        if(client != client_socket):
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)


def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0',12345))
    server_socket.listen(5)
    print("Server listening on port 12345")
    
    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        print(f"Connection from {addr}")
        client_handler = threading.Thread(target=handle_client,args=(client_socket,addr))
        client_handler.start()

if __name__ == "__main__":
    server_program()
