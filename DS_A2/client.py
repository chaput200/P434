#CASSANDRA CHAPUT
#CSCI-P434
#ASSIGNMENT 2

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
    #pass
    return data.decode()


if __name__ == '__main__':
    #DEFINE SERVER ADDRESS
    HOST = "127.0.0.1"
    PORT = 9889

    print("CMDS:\n map_wc(doc_id)\n run_mapred(input_data, map_wc, run_mapred, output_location)\n invert_index(file_dict)\n quit\n")
    cmd = input("ENTER <CMD>: ")
    #cmd = "map_wc"
    while (cmd != "quit"):
        file_dict = {} 
        # SET KEY VALUE IN FUNC SET()        
        if (cmd == "map_wc" or cmd == "MAP_WC" or cmd == "Map_wc"):
            wc_list = []
            doc_id = input("ENTER <DOCUMENT NAME>: ")
            #doc_id = "doc_1.txt"
            cmd = "map_wc"
            wc_list = send_message(f"{cmd}: {doc_id}")
            print(f"MAPPING WORD COUNT STORED IN wc_list")
        elif (cmd == "RUN_MAPRED" or cmd == "run_mapred" or cmd == "run_mapRed"):
            
            input_data = input("ENTER <WORD LIST NAME> TO BE REDUCED: ")
            #input_data = doc_wc_list
            output_location = input("ENTER <NAME OF FILE TO STORE RESULTS>: ")
            #output_location = "results.txt"
            cmd = "run_mapred"
            data_dict = send_message(f"{cmd}: {input_data} OUTPUT_LOCATION:{output_location}")
            data_dict = eval(data_dict)
            for key in data_dict:
                value = data_dict[key]
                print(f"THE WORD {key} APPEARS {value} TIMES")
        elif (cmd == "INVERT_INDEX" or cmd == "invert_Index" or cmd == "invert_index"):
            output_location = input("ENTER <NAME OF FILE TO STORE RESULTS>: ")
            fileNames = input("ENTER <NAME OF MAP RESULT FILES>: ")

            cmd = "invert_index"
            data_dict = send_message(f"{cmd}: {fileNames} OUTPUT_LOCATION:{output_location}")
            data_dict = eval(data_dict)
            print(f"IN THESE FILES: {fileNames}")
            for key in data_dict:
                value = data_dict[key]
                print(f"THE WORD {key} APPEARS {value} TIMES")
        elif (cmd == "quit" or cmd == "QUIT" or cmd == "Quit"):
            break
        else:
            print("ERROR: NOT A VALID CMD")
        
        print("\nCMDS:\n map_wc(doc_id)\n run_mapred(input_data)\n invert_index(file_dict)\n quit\n")
        cmd = input("ENTER <CMD>: ")

