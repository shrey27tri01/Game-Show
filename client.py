import socket
import time
import select
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
print("Enter IP address of server")
host = input()
print("Enter port number")
port = input()

#connect to server
s.connect((host, int(port))) 

#receive instructions
inst1 = str(s.recv(1024), "utf-8")
print(inst1)
inst2 = str(s.recv(1024), "utf-8")
print(inst2)
inst3 = str(s.recv(1024), "utf-8")
print(inst3)
inst4 = str(s.recv(1024), "utf-8")
print(inst4)
inst5 = str(s.recv(1024), "utf-8")
print(inst5)
inst6 = str(s.recv(1024), "utf-8")
print(inst6)
inst7 = str(s.recv(1024), "utf-8")
print(inst7)

#receive questions and answers
noOfQuestions = 50
index = 0
while(index < noOfQuestions):
    question_1 = str(s.recv(1024), "utf-8")
    print(question_1)     
    question_2 = str(s.recv(1024), "utf-8")
    print(question_2)

#    if question_1 == "Hi":
#        break

#    print(data)
#    c,c1,c2=select.select([sys.stdin,s],[],[],20)
    c = select.select([s],[],[],10)[0]
   
    import msvcrt
    if msvcrt.kbhit(): 
        c.append(sys.stdin)

    if len(c) > 0:
        if c[0] == sys.stdin:
            y = input()
            s.send(str.encode(y))
        else:
            d = str(c[0].recv(1024), "utf-8")
            print(d)
            index = index + 1
            continue

    data = str(s.recv(1024),"utf-8")
    print(data)
    if data == 'Answer the Question':
        ans = input()
        time.sleep(1)
        s.send(str.encode(ans))
        index = index + 1
        result = str(s.recv(1024), "utf-8")
        print(result)
    
finalResult = str(s.recv(1024), "utf-8")
print(finalResult)
