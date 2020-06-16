def arm(n):
    oldlen=len(str(n))
    intlen=int(oldlen)
    s=0
    num=n #temporary variable to stor n as after the loop the value of n will be zero
    while(n!=0):
       n1=n%10
       p=n1**intlen
       s=s+p
       n=n//10
    if s==num:  
        print("True")
    else:
        print("False")


arm(153)
