class character():
    def __init__(s,name):
        s.name = name
        s.__life = 3
        s.__score = 0

    def intro(s):
            print(f"Name :{s.name}\nLife : {s.__life}\nScore : {s.__score}")

    def kicked(s):
            s.__score+=10

    def punched(s):
            s.__score+=5

    
    def stabbed(s):
            s.__life-=1
            

    def displaylife(s):
            return s.__life

    def displayscore(s):
            return s.__score

        

     
name = input("Enter your name : ").title()
print(f"Hello {name}\nWelcome to Super Mario")
mario = character(name)
mario.intro()
print("K : for kick\nP :for punch\nS: for stabbed\nE : for Exit")

while (True):
    life = 3    
    c = input("Enter your move : ")
    if (c.lower()=="k"):
        mario.kicked()
        print("score 10 points")
        print("new score : ",mario.displayscore())

    elif c.lower()=="p":
        mario.punched()
        print("score 5 points")
        print("new score : ",mario.displayscore())


    elif c.lower()=="e":
        q = input("Are you sure?,(Y/N)")
        if q.lower()=="y":
            break
        elif q.lower()=="n":
            continue
        else:
            print("invalid input")
        
    elif c.lower()=="s":
            count = mario.displaylife()
            mario.stabbed()
            print("Got stabbed\nLost 1 life")
            print("Life remaining :",mario.displaylife())
            if count>1:
                continue
            else:
                print("GAME OVER")
                print("your score :",mario.displayscore())
                break
            
            
    
        
        

    
