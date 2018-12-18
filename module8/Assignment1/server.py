import socket

def main():
    host = '10.10.9.55'
    port = 5001

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print("connection from: " + str(addr))
    dict = {'INR': 0, 'Dollar':1, 'Pounds':2, 'Yen':3}
    mat = [[1.0,0.014,0.11,1.58],[67.0,1.0,0.75,113.41],[89.88,1.33,1.0,142.18],[0.63,0.008,0.007,1.0]]
    while True:
        data = c.recv(1024).decode()
        datalist = data.split(" ")
        if not data:
            break
        print("From connected user: " + str(data))
        value = mat[dict[datalist[1]]][dict[datalist[4]]] * float(datalist[2])
        print("sending data: " + str(value))
        c.send(str(value).encode())
    c.close()
if __name__ == '__main__':
    main()
