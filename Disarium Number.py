def disarium(n):
    strlen=len(str(n))
    intlen=int(strlen)
    sum=0
    num=n
    for i in range(intlen,0,-1):
            n1=n%10
            power= n1**i
            sum+=power
            n=n//10
           
    if sum==num:
        print("Disarium Number")
    else:
        print("Not a disarium Number")



disarium(175) #(1^1)+(7^2)+(5^3)= 175
disarium(89)
disarium(17)
disarium(15)
disarium(1)
disarium(75)
disarium(135)
disarium(518)
