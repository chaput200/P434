#### CASSANDRA CHAPUT ####
#### ASSIGNMENT 2 README ####
#### CSCI-P434 ####
#### 2/20/2023 ####

### ASSIGNMENT 2 REPORT ###
This assignment connects a client and server through the use of a socket. The client is then prompted with command options which include the ``` map_wc ``` ``` run_mapred ``` and ``` invert_index ```
- If the user enters in the ``` map_wc ``` command they are then prompted to enter a document name to send through the map word count function. The function takes every word and places it in a tuple with a count of 1. After the mapping function is complete the user will see ``` MAPPING WORD COUNT STORED IN wc_lis ``` indicating the word count for the file has been stored locally in a list called wc_list. The propt will start again asking for a command from the list.
- if the user enters in the ``` run_mapred ``` command they are then prompted to enter the name of the list to reduce. (* I would fix this to read the file that was written to in map_wc). The next propt asks the user for the name of the file to store results in. The message is sent to the server with the function ```run_mapred ``` which takes every tuple from map_wc list and counts the occurances and stores them in a dictionary. That Dictionary stores the results (as a string which can be evaluated into a list) in a file with the name the user entered before. The propt will start again asking for a command from the list. 
- if the user enters in the ``` invert_index ``` command the next thing they are asked is the name of the files they wish to take the word count from. (* I would change this to also handle the cases in which the user hasn't put the files through the mapper and reduce functions). The propt will start again asking for a command from the list.
- If the user enters ``` quit ``` as the command, the client will disconnect.

This was tested through the use of a Makefile and text provided. There are three paragraphs, each in a diffrent file to be sent through the ```map_wc``` function then ```run_mapred``` then with all three files I run ``` invert_index```.

This is the contents of test1.txt
```
Little five is termed as the greatest college weekend. After experiencing it last year, I would have to agree Little five is amazing. I hope little five is even better than last year!
```

This is the contents of test2.txt
```
Indiana University is a basketball school. That being said I believe we are a womens basketball school. Our womens team has lost one game this entire season and we pack the hall for their games. I know these women are going to get us another banner. I hope the mens basketball team can match their energy and momentum.
```

This is the contents of test3.txt
```
Big Ten Hoosier daddy? Cause this is Indiana. Yeah we do it big. Bossing on the Big Ten you know what it is. Cause this is IU U U. This is IU U U.
```

To run the tests with these paragraphs run two windows in terminal and in one type ``` make server ``` and then in the other type ``` make client ```
