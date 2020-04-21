import socket
import sys
import time
import select

all_connections = []
all_address = []
#questions = ["Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8","Q9","Q10"]
questions = []
for i in range(50):
    questions.append("Q" + str(i+1) + " : " + "1 + " + str(i+1) + " = ? ")
#answers=[1,2,3,4,5,6,7,8,9,10]
answers = []
for j in range(50):
    answers.append(j+2)
Marks=[0,0,0,0]
response=[]


# Create a Socket ( for connecting two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = "" 
        print("Enter any port number to host the game : ") 
        port = input()
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error : " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port : " + str(port))
        s.bind((host, int(port)))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")


#handling connection from multiple playes and saving to a list
#closing previous connections when server.py file is restarted
#send instructions to players and start game
def accepting_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_address[:]
    noOfClients = 0
    while True:
        conn, address = s.accept()

        #this prevents timeout
        s.setblocking(1)

        noOfClients = noOfClients + 1
        all_connections.append(conn)
        all_address.append(address)
        if noOfClients <= 3:
#           print("Connection has been established : Client " + str(j)+" " + address[0])
#           conn.send(str.encode("Total questions are 10. First one to reach 4 points wins.First enter yes for buzzer and then answer the question.If you don't know the question just don't press buzzer"))
#           time.sleep(1)
#           conn.send(str.encode("You are Player : "+ str(j)))
#           time.sleep(1)
#           conn.send(str.encode("Welcome to the game"))
            print("Connection has been established : Client " + str(noOfClients) + " " + address[0])
            conn.send(str.encode("WELCOME TO THE GAME!!!!"))
            time.sleep(1)
            conn.send(str.encode("The questions will be asked one by one."))
            time.sleep(1)
            conn.send(str.encode("If you know the correct answer, press the BUZZER within 10 seconds after the question is asked"))
            time.sleep(1)
            conn.send(str.encode("If you press the buzzer first, you will be given a chance to provide the answer within 10 seconds."))
            time.sleep(1)
            conn.send(str.encode("If the answer is correct, you will be given 1 point, otherwise -0.5. Nobody will get a chance to answer this question again"))
            time.sleep(1)
            conn.send(str.encode("The first player to get 5 points wins. "))
            time.sleep(1)
            conn.send(str.encode("You are Player number : " + str(noOfClients)))
            time.sleep(1)

        else:
#            print("Connection has been established : Client " + str(noOfClients) + " " + address[0])
            print("Maximum Clients connected")
            conn.send(str.encode("WELCOME TO THE GAME!!!!"))
            time.sleep(1)
            conn.send(str.encode("The questions will be asked one by one."))
            time.sleep(1)
            conn.send(str.encode("If you know the correct answer, press the BUZZER within 10 seconds after the question is asked"))
            time.sleep(1)
            conn.send(str.encode("If you press the buzzer first, you will be given a chance to provide the answer within 10 seconds."))
            time.sleep(1)
            conn.send(str.encode("If the answer is correct, you will be given 1 point, otherwise -0.5. Nobody will get a chance to answer this question again."))
            time.sleep(1)
            conn.send(str.encode("The first player to get 5 points wins."))
            time.sleep(1)
            conn.send(str.encode("You are Player number : " + str(noOfClients)))
            time.sleep(1)
            thread_function()
            break

# Function for handling Marks and questions                
def thread_function():   
    for i in range(len(questions)):
        for conn in all_connections:
            time.sleep(0.1)
            conn.send(str.encode(questions[i]))
            conn.send(str.encode("Press the buzzer only if you know the answer"))
        response1 = select.select(all_connections,[],[],10)
        
        if(len(response1[0]) > 0):            
            conn_name = response1[0][0]
            b = conn_name.recv(1024)
            b = b.decode("utf-8")
#            b = str(conn_name.recv(1024), "utf-8")
            response1 = ()
            for conn in all_connections:
                if conn != conn_name:
                    conn.send(str.encode("Sorry, player " + str(all_connections.index(conn_name) + 1) + " has pressed the buzzer."))
            for j in range(len(all_connections)):
                if all_connections[j] == conn_name:
                    responder = j

#            if b=='Yes' or b=='yes' or b=='YES' or b=='y':
            if b == 'y':
                conn_name.send(str.encode("Answer the Question"))
                answer = str(conn_name.recv(1024), "utf-8")

                if answer == str(answers[i]):                    
                    Marks[responder] = Marks[responder] + 1
                    conn_name.send(str.encode("Correct Answer, You get 1 Point !!!"))
                    if Marks[responder] >= 5:
                        #for c in all_connections:
                        #    c.send(str.encode("Hi"))
                        #    time.sleep(1)
                        #    break
                        return
                else:
                    conn_name.send(str.encode("Wrong Answer, You get -0.5 points"))
                    Marks[responder] = Marks[responder] - (0.5)
                    time.sleep(1)
            
            elif b == str(answers[i]):
                conn_name.send(str.encode("You didn't press the buzzer before answering. You get -1 points"))
                Marks[responder] = Marks[responder] - 1
                time.sleep(1)
        else:
            for c in all_connections:
                c.send(str.encode("Nobody pressed the buzzer. Moving on..."))

# Start program and declare winner.
def main():
    create_socket()
    bind_socket()
    accepting_connections()
    winnerMarks = 0
    winner = 0
    for i in range(len(all_connections)):
        if Marks[i] > winnerMarks:
            winner = i
            winnerMarks = Marks[i]
    
    print("Scoreboard : ")
    for i in range(len(all_connections) - 1):
        print("Player " + str(i+1) + " : " + str(Marks[i]) + " points")
    
    for c in all_connections:
        if all_connections.index(c) != winner:
            c.send(str.encode("The winner is Player: " + str(winner + 1) + " with " + str(winnerMarks) + " points" ))
        else:
            c.send(str.encode("Congratulations! You are the winner with " + str(winnerMarks) + " Points" ))
main()