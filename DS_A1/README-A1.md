#### CASSANDRA CHAPUT ####
#### ASSIGNMENT 1 README ####
#### CSCI-P434 ####
#### 1/31/2023 ####

### ASSIGNMENT 1 REPORT ###

### THINGS I WOULD MODIFY ###
1. I would put a try and catch for writing to a text file, the code I would put would be more like this
``` 
try:
	f=open('data_dictionary.txt', 'w')
        f.write(str(data_dict.items()))
        f.close()
except:
	print("ERROR: UNABLE TO WRITE TO TXT FILE")
``` 
2. I do not know how to make a makefile and so I would love for that to be a modification. 
3. the clint only can do one command or else the program ends, I would love to fix that so you have as many commands as you want.


### ERRORS NOT HANDLED  ###
1. If a key already in the dictionary is used in the set command 
2. the case of the strings matter, maybe change that to just accept any case of the string
3. the get command does not work.

