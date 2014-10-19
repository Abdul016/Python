

name=input("What is your Name? ")

print("Hello " + name + "Let's play a game!")

print("Think of random number from 1 to 100, and I'll try to guess it!")



play = True
guess = False
tries = 1

while(play != False):
    a = 1
    b = 50
    c =  100
    
    while (guess != True): 
        equal = input("Is it %d? (yes/no)" %b)
        if (equal == "yes"):
            print("Got it")
            print("I got it in"+str(tries)+"tries")
            break
        elif(equal == "no"):
            tries= tries+1
            greater=input("is it greter than %d?(yes/no)"%b)
            if(greater == "yes"):
                a = b + 1
                
            elif (greater == "no"):
                c = b - 1 
            
            b = ((a + c)/2) 
        
        
    more = input("Do you want to play more? ")
    if(more == "yes"):
        play = True
    elif (more == "no"):
        play = False
        
        print("Bye Bye")
