import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345

    sock.connect((host, port))

    print("Enter a msg : ", end='')
    msg = input()
    sock.send(msg.encode())
    sock.close()

    return 0


if __name__ == '__main__':
    main()