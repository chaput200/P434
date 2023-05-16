#### CASSANDRA CHAPUT ####
#### ASSIGNMENT 2 README ####
#### CSCI-P434 ####
#### 2/20/2023 ####

### ASSIGNMENT DistKV REPORT ###
I implememented a makefile with commands to run in a total of three windows.
The first window will run the ``` make primary ``` command.
- This will prompt the clients to tell the replicate 0 a key and value to store. The first item is key m and value kolodin. The replicate sends the info to the primary and the primary updates. The primary sends the new dict back and so the replicate has an updated data set. 
The second window will run the ``` make replica0 ``` command
- This starts the replica up with two ports open, one for getting requests and another for a connection to the primary. 
Finally the ``` make client0 ``` and ``` make client1 ``` commands both run set key values to the replica0.


This is an implementation of the primary based replication and a sequential consistency implemenation. This is because all writes are immediate and update the replicates after adding an item, meaning before a read. Since we do not use blocking this isn't linearization. Additionally to achieve causal consistency some read request would be allowed to read from the replicates current dictionary of the data_dict. This would indicate that reads must just occur after a local write and before the rest of the writes are sent. 

One of the main challenges in this assignment was being able to differenciate between sequential or causal consistency. This was because the processes would have updated in order to be able to use the get request. I also felt it was hard to find test data to implement these consistency models. Conceptually we have covered these really well, however actually coding them felt like a major diconnect. I had very little to no background on sockets and how to use them so this class itself was very challenging. Not to mention there isn't alot of examples of these consistency models in programming. Overall I felt lost for the majority of the project honestly.
