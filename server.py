
import socket
import threading
import time
import pickle
import winsound

import numpy
import matplotlib.pyplot as plt
from multiprocessing import Process

sensor1_list = []
sensor2_list = []

adder1 = None
adder2 = None


def sufficient_data():
    time.sleep(1)

    if len(sensor1_list) < 20:
        return True

    else:
        return False

def sufficient_data2():
    time.sleep(1)

    if len(sensor2_list) < 20:
        return True

    else:
        return False

def BIGDATA2():
    data = sensor2_list
    x_data1 = []
    y_data1 = []
    x_data2 = []
    y_data2 = []



    for i in data:
        if isinstance(i, list):


            if i[0] == 0:
                x = i[1]+5
                y = i[2]+1.5
                #print(x)
                #print(y)
                x_data1.append(round(x, 4))
                y_data1.append(round(y, 4))



            if i[0] == 1:
                x = i[1]+8
                y = i[2]+1.5
                x_data2.append(round(x, 4))
                y_data2.append(round(y, 4))
    if len(x_data1) >= 20:
        del(x_data1[0:9])

    return x_data1, y_data1, x_data2, y_data2



def BIGDATA():

    data = sensor1_list
    #print(sensor1_list)
    x_data1 = []
    y_data1 = []
    x_data2 = []
    y_data2 = []


    #clean_data("sen1")

    for i in data:
        if isinstance(i, list):

            if i[0] == 0:
                x = i[1]+2.5
                y = i[2]+1.5
                x_data1.append(round(x, 2))
                y_data1.append(round(y, 2))

            if i[0] == 1:
                pass
                '''
                x = i[1]
                y = i[2]
                x_data2.append(round(x + 3, 2))
                y_data2.append(round(y + 3, 2))
                '''
    if len(x_data1) >= 20:
        del(x_data1[0:9])
    return x_data1, y_data1 , x_data2, y_data2


# ports above 4000 are unused I think
PORT = 5060
HEADER = 10000  # 64 bytes are allocated to specify length of the next msg
FORMAT = 'utf-8'
# SERVER = "192.168.0.7"
# ^ hard coded IP bad practice

#DISCONNECT_MSG = "ur doneeee go ahead and log off for me"

# automatically get IPV4
SERVER = socket.gethostbyname(socket.gethostname())  # pulls ur IP little buddy

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AS FUCK
#                       Family         Type

ADDR = (SERVER, PORT)
server.bind(ADDR)


def handle_client(conn, addr):
    global adder2, adder1
    print(f"[you connected with] {addr}")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)  # length of our message
        if msg_length:  # if msg not none
            msg_length = int(msg_length)
            msg = pickle.loads(conn.recv(msg_length))  # de-pickling the list
            if msg == "Sensor 1 connecting...":
                adder1 = addr[1]  # this is address of sensor 1
                print('this is sensor 1 ', addr[1])
            if msg == "Sensor 2 connecting...":
                adder2 = addr[1]  # this is address of sensor 2
                print('this is sensor 2')
            if addr[1] == adder1:
                sensor1_list.append(msg)
            if addr[1] == adder2:
                sensor2_list.append(msg)
            conn.send("server got your message".encode(FORMAT))
    conn.close()


# handles new connections
def start():
    server.listen()
    print(f"The server listening on {SERVER}")
    winsound.Beep(580, 1000)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # threads for multiple communications
        thread.start()
        print(f"{threading.active_count() - 1 }  [is connected ]")
        # one thread always will be running ie we subtract one

def startserver():
    print("the server is starting")
    start()





