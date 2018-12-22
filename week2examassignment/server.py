import socket
from threading import *
import os
import signal
import time
students = {"20158501" : ["What is my first vehicle first number?", "501"],
            "20158502" : ["What is my masters degree?", "MSIT"],
            "20158503" : ["Who is my close friend?", "Sriram"],
            "20158504" : ["When did you meet your close friend?", "1999"],
            "20158505" : ["Whatâ€™s your mother's maiden name?", "John"],
            "20158506" : ["Who invented telephone?", "Graham Bell"],
            "20158507" : ["Who invented radium?", "Madam Curie"],
            "20158508" : ["Which country is called as land of rising sun?", "Japan"],
            "20158509" : ["Which country is called of white elephants?", "Thailand"],
            "20158510" : ["Gateway of India?", "Mumbai"]}
s = socket.socket()

def main():
    host = "10.10.9.55"
    port = 7059
    s.bind((host, port))
    s.listen(1)
    print("Server started..! at: "+str(host))
    while True:
        connection, addr = s.accept()
        Thread(target = clients, args = (connection,)).start()
    s.close()

def clients(connection):
    request = connection.recv(1024).decode()
    data = request.split(" ")
    if data[1] not in students.keys():
        mes = "ROLLNUMBER-NOTFOUND"
        connection.send(mes.encode())
    elif data[0] == "MARK-ATTENDENCE" and data[1] in students.keys():
        mes = "SECRETQUESTION - " + students[data[1]][0]
        connection.send(mes.encode())
    reply = connection.recv(1024).decode()
    if reply == students[data[1]][1]:
        mes = "ATTENDANCE-SUCCESS"
        connection.send(mes.encode())
    else:
        failure(connection,data)
def failure(connection,data):
    mes = "SECRETQUESTION - " + students[data[1]][0]
    connection.send(mes.encode())
    reply = connection.recv(1024).decode()
    if reply == students[data[1]][1]:
        mes = "ATTENDANCE-SUCCESS"
        connection.send(mes.encode())
    else:
        failure(conection,data)
if __name__ == '__main__':
    main()

