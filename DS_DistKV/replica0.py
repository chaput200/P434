"""
CASSANDRA CHAPUT
CSCI-P434

REPLICA0.PY
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



#FUNCTION TO GET THE ITEM FROM DICT W THAT KEY
def sendToPrimary(message):
    #CREATE SOCKET VAR
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.connect((HOST,9887))
    s.sendall(message.encode())
    data = s.recv(1024)
    print(f"RECIEVED DATA IS {data.decode()}")
    d = data.decode()
    d_items = d.split(" ")
    d_items.remove(d_items[-1])
    #print(d_items)
    for item in d_items:
        i = item.split(":")
        k = i[0]
        v = i[1]
        data_dict[k]=v
    print("DATA DICT IS ",data_dict.items())
    #SAVE TO DATA_DICT FOR REPLICATE
    msg = "STORED"
    conn.sendall(msg.encode())
    s.close()
    return data.decode()

if __name__ == '__main__':
    #DEFINE SERVER ADDRESS
    HOST = ''
    #PORT = 9889
    #BIND SERVER TO ADDY AND LISTEN FOR CLIENT
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    #s.setblocking(0)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #socket.sethostname("replica0")
    s.bind((HOST, 9889))
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
        print(f"CLIENT CONNECTED BY {addr}")
        #conn.setblocking(0)
        #ADD TO INPUTS LIST & QUEUE
        inputs.append(conn)
        print(f"INPUTS: {inputs}")
        #GET DATA FROM CLIENT
        data = conn.recv(1024)
        #data = recvall(conn)

        #PRINT RECIEVED DATA
        print(f"ADDRESS {addr} \nDATA: {data.decode()}")

        #DETERMINE WHICH REPLICA TO TALK TO 
        #DETERMIND CMD & KEY
        l = list(data.decode().split(" "))
        print("DATA DECODED IS : ", l)
        m = l[1]+" "+l[2]+" "+l[3]
        sendToPrimary(m)
        #conn.sendall(f"UPDATED DICT: {data_dict.items()}".encode())
        #print(f"STORED\r\n")
        #return data_dict

