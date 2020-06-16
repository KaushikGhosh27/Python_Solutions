import random

##n = random.choice(["r","p","s"])
##
##m = input("r,s,or p: ")
##print(n)
##if n == m:
##    print("yes")

def game():
    uscore = 0
    cscore = 0
    while uscore<5 and cscore<5:
        user = input("Enter choice(R or S or P): ").upper()
        computer = random.choice(["R","P","S"])
        if user == computer:
            uscore+=0
            cscore+=0
        elif user == 'S' and computer=='P':
            uscore +=1
        elif user == 'S' and computer=='R':
            cscore+=1
        elif user == 'R' and computer == 'S':
            uscore+=1
        elif user== 'R'and computer == 'P':
            cscore+=1
        elif user == 'P'and computer == 'R':
            uscore+=1
        elif user == 'P' and computer == 'S':
            cscore+=1
        else:
            print("Invalid input")

        print(computer)
        print("User: {} Computer: {}".format(uscore,cscore))
        print()
    if uscore == 5:
        print("User won")
    elif cscore == 5:
        print("Computer won")


game()
        
