import socket
import random
import threading

def main():
    host = '10.10.9.55'
    port = 7025

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    while True:
        c, addr = s.accept()
        print("connection from: " + str(addr))
        string = "      Welcome to Guess My Number      "
        string1 = "I'm thinking of a number between 1 and 100. Try to guess it in as few attempts as possible"
        c.send(string.encode())
        c.send(string1.encode())
        threading.Thread(target = game, args = (c, addr)).start()

def game(c, addr):
    num = random.randint(1,101)
    c.send(str(num).encode())
    count = 0
    while True:
        data = c.recv(1024).decode()
        print("Guess: " + str(data))
        if not data:
            break
        if int(data) == num:
            count += 1
            send = "Correct, number of guess: " + str(count)
            c.send(send.encode())
            break
        elif int(data) < num:
            count += 1
            send = "Your number is less than the guess"
            c.send(send.encode())
        elif int(data) > num:
            count += 1
            send = "Your number is greater than the guess"
            c.send(send.encode())
    print("Server Closed")   
    c.close()
if __name__ == '__main__':
    main()
