import socket

def main():
    host = '10.10.9.55'
    port = 7025

    s = socket.socket()
    s.connect((host,port))
    string = s.recv(1024).decode()
    string1 = s.recv(1024).decode()
    num = s.recv(1024).decode()
    print("Connecting to Server...\n")
    print("connected!\n")
    print(str(string))
    print(str(string1) + "\n")
    message = input("Enter your guess: ")
    while message != 'q':
        s.send(message.encode())
        data = s.recv(1024).decode()
        print(str(data))
        if num == message:
        	break
        message = input("Enter your guess: ")
    s.close()
if __name__ == '__main__':
    main()