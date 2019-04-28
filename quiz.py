import time
points = 0
nam = str(input("Please enter your name :"))
print("Hello " +nam+ " Welcome !")

def q1():
    global points
    print("\n1.Python was designed by : ")
    print("a. Ken Thompson")
    print("b. Dennis Ritchie")
    print("c. Guido Van Roussam")
    ans=str(input("Please enter your answer : "))
    if(ans=='c' or ans=='C'):
        print("Your answer is correct")
        points=points+1
    else:
        print("Sorry! Thats the wrong answer")
    q2()
def q2():
    global points
    time.sleep(0.5)
    print("\n2.Which of the following is not a core datatype in python ")
    print("a. Class")
    print("b. List")
    print("c. Tuple")
    ans=str(input("Please enter your answer : "))
    if(ans=='a' or ans=='A'):
        print("Your answer is correct")
        points=points+1
    else:
        print("Sorry! Thats the wrong answer")
    q3()
def q3():
    global points
    time.sleep(0.5)
    print("\n3.How can a list be defined in python : ")
    print("a. using {}")
    print("b. using ()")
    print("c. using []")
    ans=str(input("Please enter your answer : "))
    if(ans=='c' or ans=='C'):
        print("Your answer is correct")
        points=points+1
    else:
        print("Sorry! Thats the wrong answer")
    q4()
def q4():
    global points
    time.sleep(0.5)
    print("\n4.Python is a case sensitive language : ")
    print("a. No")
    print("b. Yes")
    ans=str(input("Please enter your answer : "))
    if(ans=='b' or ans=='B'):
        print("Your answer is correct")
        points=points+1
    else:
        print("Sorry! Thats the wrong answer")
    q5()
def q5():
    global points
    time.sleep(0.5)
    print("\n5.Python was developed in  : ")
    print("a. 1984")
    print("b. 1986")
    print("c. 1991")
    ans=str(input("Please enter your answer : "))
    if(ans=='c' or ans=='C'):
        print("Your answer is correct")
        points=points+1
    else:
        print("Sorry! Thats the wrong answer")
    q6()
def q6():
    global points
    time.sleep(0.5)
    print("\n6.The output for the following snippet will be\n" "print(type(a))")
    print("a. int")
    print("b. string")
    print("c. float")
    ans=str(input("Please enter your answer : "))
    if(ans=='a' or ans=='A'):
        print("Your answer is correct")
        points=points+1
    else:
        print("Sorry! Thats the wrong answer")
time.sleep(1)

q1()


if(points>=5):
    print("\nCongratulations! Excellent Job")
    print("Your score is ",points)    
elif(3>points<5):
    print("Very Good.")
    print("Your score is ",points)    
elif(1>points<3):
    print("Good")
    print("Your score is ",points)    
else:
    print("Try to improve")
    print("Your score is ",points)    
print("\nThanks for taking the quiz "+nam)
