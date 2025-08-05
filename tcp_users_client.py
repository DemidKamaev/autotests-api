import socket


def first_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_address = ('localhost', 12345)
    client_socket.connect(client_address)

    message = "Привет, сервер!"
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(response)
    client_socket.close()


def second_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_address = ('localhost', 12345)
    client_socket.connect(client_address)

    message = "Как дела?"
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(response)
    client_socket.close()


if __name__ == '__main__':
    first_client()
    second_client()
