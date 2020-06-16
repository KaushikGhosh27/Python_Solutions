def armstrong(n):
    strlen=len(str(n))
    intlen=int(strlen)
    num=n
    sum=0
    while(n!=0):
        n1 = n%10
        power = n1**intlen
        sum = sum+power
        n=n//10
    if sum == num:
        return True
def myrange(lb,ub):
    for i in range(lb,ub+1):
        if armstrong(i):
            print(i)


lb =  int(input("Enter lower bound: "))
ub = int(input("Enter upper bound: "))
print("\nArmstrong numbers in the given range: ")
myrange(lb,ub)
