#CASSANDRA CHAPUT
#CSCI-P434

#CLIENT0.PY

#IMPORT STATEMENTS
import socket
# FUNCTION TO COMMUNICATE W SERVER
# PARAMETER: MESSAGE TO SEND TO SERVER
def send_message(message):
    #CREATE SOCKET VAR
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    s.sendall(message.encode())
    data = s.recv(1024)
    print(f"{data.decode()}")
    s.close()
    pass


if __name__ == '__main__':
    #DEFINE SERVER ADDRESS
    #HOST = ''
    #PORT = 9889

    print("CMS:\n get(replica, key, value)\n set(replica, key, value)\n quit\n")
    print("VALID REPLICAS: R0, R1")
    #rep_cmd = input("ENTER <REPLICA> <CMD>: ")
    rep_cmd = "r0 set"
    l = list(rep_cmd.split(" "))
    rep = l[0]
    cmd = l[1]
    print(f"REP: {rep} CMD {cmd}")
    while (cmd != "quit"):
        #ID REPLICA TO CONNECT TO
        if (rep == "r0" or rep == "R0"):
            HOST = ''
            PORT = 9889
        elif (rep == "r1" or rep == "R1"):
            HOST = ''
            PORT = 9888
        # SET KEY VALUE IN FUNC SET()        
        if (cmd == "set" or cmd == "SET" or cmd == "Set"):
            #item = input("ENTER <KEY> <VALUE>: ")
            item = "m kolodin"
            send_message(f"{rep_cmd} {item}")
        elif (cmd == "get" or cmd == "GET" or cmd == "Get"):
            item = input("ENTER <KEY>: ")
            send_message(f"{rep_cmd} {item}")
        elif (cmd == "quit" or cmd == "QUIT" or cmd == "Quit"):
            send_message(f"{rep_cmd}")
        else:
            print("ERROR: NOT A VALID CMD")

        #print("CMS:\n get(key, value)\n set(key, value)\n quit\n")
        print("CMS:\n get(replica, key, value)\n set(replica, key, value)\n quit\n")
        print("VALID REPLICAS: R0, R1")
        rep_cmd = input("ENTER <REPLICA> <CMD>: ")
        l = list(rep_cmd.split(" "))
        rep = l[0]
        cmd = l[1]
        
    
