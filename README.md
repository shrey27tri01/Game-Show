# Game-Show
A game show implemented in python using socket programming

#### INSTRUCTIONS TO RUN THE PROGRAM:    
● Save the two files server.py and client.py at a location.   
● Open command terminal, go to the location where the server file is saved, and type **​python3 server.py**   
● Enter any port number to host the game (eg. 64). A message will come: “Binding the Port”. If not, try again.   
● Then simultaneously open **​four more​** command terminals and go to the location where client file is saved on all of them. (We won’t be using the fourth one)   
● Type **​python3 client.py** ​on all the four terminals    
● Enter the IP address (eg. 127.0.0.1) and port number (eg. 64) of the host **on all the four command terminals**    
● Once you enter the IP address and port number on the fifth (last) command terminal, **​minimise it, since it is of no use to us, but do not close it.**    
● Now read the instructions on the three client windows and the questions will start coming.   
● To answer a question press the buzzer, that is **​press y and then Enter ​(​NOTE:** ​Once you press y and then Enter once, you will have to wait​ ​until the 10 second window closes. Only then will you be told to answer the question. Hence, press the buzzer once then wait for some time.)   
● You have 10 seconds to press the buzzer once a question comes on the screen, else it will move on to the next question.   
● Once you press the buzzer, you will be told to give the answer. To answer the question, **​type the answer and press enter.** ​If it is correct, you will be awarded 1 point, else -0.5 points.    
● If you give correct answer but without the buzzer, 1 point will be deducted from your score.   
● The first player of the three to reach 5 points will be declared the winner.   
● After the game ends, scoreboard will be displayed on the server screen and each client will be notified if he has won, or who the winner is. 
 
