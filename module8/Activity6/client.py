import socket
def main():
    host = '10.2.138.107'
    port = 5050

    server = ('10.10.9.55', 5051)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input("--->")
    while message != 'q':
        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        print("Received from server: " + str(data).decode())
        message = input("--->")
    s.close()
if __name__ == '__main__':
    main()
