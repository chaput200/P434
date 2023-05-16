#CASSANDRA CHAPUT
#CSCI-P434
#ASSIGNMENT 1

#CLIENT.PY

#IMPORT STATEMENTS
import socket

# FUNCTION TO COMMUNICATE W SERVER
# PARAMETER: MESSAGE TO SEND TO SERVER
def send_message(message):
    #CREATE SOCKET VAR
    s = socket.socket()
    s.connect((HOST,PORT))
    s.sendall(message.encode())
    data = s.recv(1024)
    print(f"{data.decode()}")
    s.close()
    pass


if __name__ == '__main__':
    #DEFINE SERVER ADDRESS
    HOST = "127.0.0.1"
    PORT = 9889

    print("CMS:\n get(key, value)\n set(key, value)\n quit\n")
    cmd_key = input("ENTER <CMD> <KEY>: ")
    l = list(cmd_key.split(" "))
    cmd = l[0]

    while (cmd != "quit"):
        # SET KEY VALUE IN FUNC SET()        
        if (cmd == "set" or cmd == "SET" or cmd == "Set"):
            value = input("ENTER <VALUE>: ")
            send_message(f"{cmd_key} {value}")
        elif (cmd == "get" or cmd == "GET" or cmd == "Get"):
            send_message(f"{cmd_key}")
        elif (cmd == "quit" or cmd == "QUIT" or cmd == "Quit"):
            break
        else:
            print("ERROR: NOT A VALID CMD")

        #print("CMS:\n get(key, value)\n set(key, value)\n quit\n")
        cmd_key = input("ENTER <CMD> <KEY>: ")
        l = list(cmd_key.split(" "))
        cmd = l[0]
