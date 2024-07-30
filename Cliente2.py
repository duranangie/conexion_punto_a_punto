import socket
import threading

def receive_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Other: {message}")
            else:
                break
        except:
            break


def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("Enter server IP: ")
    server_port = 12345
    client_socket.connect((server_ip, server_port))

    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    receive_thread.start()


    while True:
        message = input("You: ")
        if message.lower()=="quit":
            break
        client_socket.send(message.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    client_program()
