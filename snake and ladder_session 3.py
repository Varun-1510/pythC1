import random
count=0
while(count<=100):
    n=input("press R to roll dice")
    if(n=="r"):
        r=random.randint(1,6)
    count=count+r
    print("your random num is",r)
    print("your count num is",count)
    if count==8:
        count=37
        print("WOW!!,U have climbed the ladder and count is",count)
    if count==13:
       count=34
       print("WOW!!,U have climbed the ladder and count is",count)
    if count==40:
       count=68
       print("WOW!!,U have climbed the ladder and count is",count)
    if count==52:
       count=8
       print("WOW!!,U have climbed the ladder and count is",count)
    if count==76:
       count=97
       print("WOW!!,U have climbed the ladder and count is",count)
    elif count==11:
         count=2
         print("OOPS!!,U are bit by the snake and count is",count)
    elif count==25:
         count=4
         print("OOPS!!,U are bit by the snake and count is",count)
    elif count==38:
         count=9
         print("OOPS!!,U are bit by the snake and count is",count)
    elif count==65:
         count=46
         print("OOPS!!,U are bit by the snake and count is",count)
    elif count==89:
         count=70
         print("OOPS!!,U are bit by the snake and count is",count)
    elif count==93:
         count=64
         print("OOPS!!,U are bit by the snake and count is",count)
    elif count>=100:
        print("U HAVE WON!!!")
    else:
        print("CONTINUE THE GAME")
