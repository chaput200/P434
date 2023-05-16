"""
CASSANDRA CHAPUT
CSCI-P434

PRIMARY.PY
"""

#IMPORT STATEMENTS
import socket
import select
import sys
import queue

#GLOBAL DICTIONARY
data_dict = {}

# FUNCTION TO GET DATA FROM SOCKET
# PARAMETER: SOCK(CONNECTION OF CLIENT)
# RETURN DATA SENT BY CLIENT
def recvall(sock):
    BUFF_SIZE = 10 #1 KiB
    data = b''
    while True:
        chunk = sock.recv(BUFF_SIZE)
        data += chunk
        if len(chunk) < BUFF_SIZE:
            #EITHER 0 OR EOD
            break
    return data

# FUNCTION TO SET INPUT INTO DICT
def set(key, value):
    if key in data_dict.keys():
        data_dict[key] = data_dict[key]+value
    else:
        data_dict[key] = value
    #SEND DATA BACK TO CLIENT
    allItems = ''
    for k in data_dict.keys():
        v = data_dict.get(k)
        allItems=allItems+k+':'+v+' '
    conn.sendall(f"{allItems}".encode())
    print(f"STORED\r\n")
    return data_dict

#FUNCTION TO GET THE ITEM FROM DICT W THAT KEY
def get(key):
    if key in data_dict.keys():
        print(f"FOUND {key} IN DICTIONARY KEYS!\nKEY: {key}\nVALUE: {data_dict[key]}")
    conn.sendall(f"RETURN DATA FOR ID: {key} {data_dict[key]}".encode())
    print("END\r\n")

if __name__ == '__main__':
    #DEFINE SERVER ADDRESS
    HOST = ''
    #PORT = 9887
    #BIND SERVER TO ADDY AND LISTEN FOR CLIENT
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    #s.setblocking(0)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, 9887))
    s.listen()
    # LIST OF CLIENTS & THEIR ADDRESSES
    inputs = [s]

    #DEFINE CMD, KEY & VALUE
    rep = ''
    cmd = ''
    key =''
    value = ''

    while True:        
        conn , addr = s.accept()
        print(f"CONNECTED BY {addr}")
        #conn.setblocking(0)
        #ADD TO INPUTS LIST & QUEUE
        inputs.append(conn)
        print(f"INPUTS: {inputs}")
        #print(f"SOCK NAME IS {conn.getsockname()}")
        print(f"CONNECTED BY {addr}")
        #GET DATA FROM CLIENT
        data = conn.recv(1024)
        #data = recvall(conn)

        #PRINT RECIEVED DATA
        print(f"ADDRESS {addr} \nDATA: {data.decode()}")

        #DETERMINE WHICH REPLICA TO TALK TO 
        #DETERMIND CMD & KEY
        l = list(data.decode().split(" "))
        print("DATA DECODED IS : ", l)

        cmd = l[0]

        # SET KEY VALUE IN FUNC SET()
        if cmd == "set":
            set(l[1],l[2])
        elif cmd == "get":
            get(l[1])
        print(data_dict.items())

