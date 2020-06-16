def ratiopnz(array):
    pcount = 0
    ncount = 0
    zcount = 0
    for i in array:
        if i>0:
            pcount+=1
        elif i==0:
            zcount+=1
        elif i<0:
            ncount+=1
    tcount=pcount+zcount+ncount
    pratio = pcount/tcount
    nratio = ncount/tcount
    zratio = zcount/tcount
    print(pratio)
    print(nratio)
    print(zratio)

n=int(input("Enter the no. of elements you would like to enter: "))
array=[]
for i in range(n):
    a=int(input("Enter element: "))
    array.append(a)

ratiopnz(array) 
