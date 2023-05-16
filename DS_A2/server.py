"""
CASSANDRA CHAPUT
2/21/2023
CSCI-P434
ASSIGNMENT 2

SERVER.PY
"""



#IMPORT STATEMENTS
import socket

#GLOBAL DICTIONARY & LIST
wc_list = []
reduced_dict = {}

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

# FUNCTION TO MAP WORDCOUNT OF FILE
def map_wc(doc_id):
    wc_list.clear()
    with open(doc_id, 'r') as doc:
        for line in doc: 
            line.strip()
            #print("LINE: ", line)
            for word in list(line.split(" ")): 
                word = word.lower()
                word = word.replace(",", "")
                word = word.replace(".", "")
                word = word.replace(";", "")
                word = word.replace("!", "")
                word = word.replace("?", "")
                tup = tuple((word.strip(), 1))
                wc_list.append(tup)
                #print("WORD: ", word)
    conn.sendall(f"{wc_list}".encode())
    return wc_list

def set(dictionary, key, value):
    if key in dictionary.keys():
        dictionary[key] = dictionary[key]+value
    else:
        dictionary[key] = value
    return dictionary

# FUNCTION TO REDUCE 
def run_mapred(input_data, output_location):
    reduced_dict.clear()
    res = eval(input_data)
    for t in res:
        #print(t)
        #print(type(t))
        set(reduced_dict, t[0], t[1])
    
    # CREATE OUTPUT FILE
    text = str(list(reduced_dict.items()))
    output_file = open(output_location, 'w')
    output_file.write(text)
    output_file.close()

    conn.sendall(f"{reduced_dict}".encode())
    return reduced_dict

# FUNCTION FOR INVERT INDEX
def invert_index(file_list, output_location):
    mult_file_wc = {}
    for file_name in file_list:
        f = open(file_name, 'r').read()
        wc = eval(f)
        for item in wc:
            mult_file_wc = set(mult_file_wc, item[0], item[1])
    
    # CREATE OUTPUT FILE
    output_file = open(output_location, 'w')
    text = str(list(mult_file_wc.items()))
    output_file.write(text)
    output_file.close()

    conn.sendall(f"{mult_file_wc}".encode())
    return mult_file_wc


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
        print(f"ADDRESS {addr} \n CMD: {data.decode()}")

        #DETERMIND CMD & KEY
        l = list(data.decode().split(": "))
        cmd = l[0]

        # SET KEY VALUE IN FUNC SET()
        if cmd == "map_wc":
            map_wc(l[1])
        elif cmd == "run_mapred":
            l1 = list(l[1].split(" OUTPUT_LOCATION:"))
            input_data = l1[0]
            #print("TYPE OF INPUT_DATA IS ", type(input_data))
            output_location = l1[1] 
            run_mapred(input_data, output_location)
        elif cmd == "invert_index":
            l1 = list(l[1].split(" OUTPUT_LOCATION:"))
            output_location = l1[1]
            file_list = list(l1[0].split(" "))
            #print(f"\nFILE LIST:{file_list[0]} {file_list[1]} {file_list[2]}\n\n")
            file_dict = {}
            for f in file_list:
                file_dict[f] = None
            invert_index(file_dict, output_location)

