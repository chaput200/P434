"""
CASSANDRA CHAPUT
2/21/2023
CSCI-P434
ASSIGNMENT 2

SERVER.PY
"""

#IMPORT STATEMENTS
import socket

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
    data_dict[key] = value
    #SEND DATA BACK TO CLIENT
    conn.sendall(f"RETURN DATA FOR ID: {key} {data_dict[key]}".encode())
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
    HOST = "127.0.0.1"
    PORT = 9889

    #DEFINE CMD, KEY & VALUE
    cmd = ''
    key =''
    value = ''

    #BIND SERVER TO ADDY AND LISTEN FOR CLIENT
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen()

    while True:
        conn, addr = s.accept()
        print(f"CONNECTED BY {addr}")

        #GET DATA FROM CLIENT
        #data = conn.recv(1024)
        data = recvall(conn)

        #PRINT RECIEVED DATA
        print(f"ADDRESS {addr} \n DATA: {data.decode()}")

        #DETERMIND CMD & KEY
        l = list(data.decode().split(" "))
        cmd = l[0]

        #DETERMIND CMD & KEY
        l = list(data.decode().split(" "))
        cmd = l[0]

        # SET KEY VALUE IN FUNC SET()
        if cmd == "set":
            set(l[1],l[2])
        elif cmd == "get":
            get(l[1])

        print(data_dict.items())

        #PERSISENT DICT
        f=open('data_dictionary.txt', 'w')
        f.write(str(data_dict.items()))
        f.close()
