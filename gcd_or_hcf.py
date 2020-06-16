def gcd(a,b):
    if a>b: #5,15
        small = a
    else:
        small = b
        
    for i in range(1,small+1):
        if(a%i==0 and b%i==0):
            hcf=i
    return(hcf)


print("HCF = ",hcf)
lcm=int((5*15)/(gcd(5,15)))
print("LCM = "+str(lcm))

#lcm= (a*b)/(gcd(a,b))
