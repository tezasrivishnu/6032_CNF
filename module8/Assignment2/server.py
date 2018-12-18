import socket
def main():
    host = '10.10.9.55'
    port = 8020

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started")
    dict = {'INR': 0, 'Dollar':1, 'Pounds':2, 'Yen':3}
    mat = [[1.0,0.014,0.11,1.58],[67.0,1.0,0.75,113.41],[89.88,1.33,1.0,142.18],[0.63,0.008,0.007,1.0]]
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode()
        datalist = data.split(" ")
        print("Message from: " + str(addr))
        print("from connected user: " + str(data))
        value = mat[dict[datalist[1]]][dict[datalist[4]]] * float(datalist[2])
        print("sending data: " + str(value))
        s.sendto(str(value).encode(), addr)
    s.close()
if __name__ == '__main__':
    main()