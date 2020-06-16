from cmath import *
def quad(a,b,c):  


    b1= (b**2)-(4*a*c)
    x= (-b + ((b1)**(1/2)))/(2*a)
    y= (-b - ((b1)**(1/2)))/(2*a)

    if b1==0:
        print("Roots are real and equal")
    elif b1>0:
       print("Roots are real and distinct")
    elif b<0:
        print("Roots are imiginary")



    print("Roots :",str(x),",",str(y))
    

a,b,c=map(float, input("Enter a,b,c: ").split(','))
quad(a,b,c)

quad(5,6,1)
quad(1,-2,1)
quad(1,6,5)
quad(1,-3,10)
