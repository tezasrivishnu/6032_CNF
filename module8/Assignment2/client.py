import socket
def main():
    host = '10.10.9.55'
    port = 8018

    server = ('10.10.9.55', 8020)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input("--->")
    while message != 'q':
        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        data = data.decode()
        print("Received from server: " + str(data))
        message = input("--->")
    s.close()
if __name__ == '__main__':
    main()
