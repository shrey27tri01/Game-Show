# Game-Show
A game show implemented in python using socket programming

#### PROJECT OVERVIEW:
There is a host who conducts a game show and participants/players who provide answers. There are three participants. The host has a long list of questions and correct answers with him. He randomly chooses one of the questions (making sure it is not a repeat of previous questions) and sends to all three players. The players receive the question, think about the answer for a while and press the buzzer. There is a timer for 10 seconds for buzzer to be pressed. Otherwise, the host moves on to the next question. The first one to press the buzzer is given a chance to provide the answer within 10 seconds. If the answer is correct, he is given 1 point, otherwise -0.5. Nobody gets chance to answer this question again. The host then proceeds with the next question. The game stops when any player gets 5 points and that player is declared the winner. 
 
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
 
#### DESCRIPTION:
 I have divided the project into two phases, the client phase and the server phase. First, the server waits for a connection from the **four clients** (of which the players are three) and then proceeds with the questions only if all the participants have joined. Each of them has been assigned as Player1, Player 2 and Player 3 with respect to the time of their participation. Then the server broadcasts the questions from the stored set of questions in the list given by initiating the ​thread_function()​ function. It then waits for buzzer to be pressed from any one of the user and then waits for the user to give some input. If the user gives a correct answer his score is incremented accordingly and reduced if it is a wrong answer. It keeps on doing the process until a player scores 5 points. Then the program is ended. 
 
 
