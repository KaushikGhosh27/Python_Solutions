def compression(s):
    count=1
    current=0
    l1=[]
    l2=[]
    for i in range(len(s)-1):
        if s[i+1]== s[current]:
            count+=1
        else:
           # print(s[current],count)
            l1.append(s[current])
            l2.append(str(count))
            current=i+1
            count=1
    #print(s[current],count)
    l1.append(s[current])
    l2.append(str(count))
    print(l1)
    print(l2)
    l3=[]
    for i in range(len(l1)):
        add = l2[i]+" "+l1[i]
        l3.append(add)
    #print(l3)
    l3.sort()
    #l3.reverse()
    #print(l3)
    for i in l3:
        print(i)
    
    


#compression("aaabbccdefggghhi")

compression("aacccddegghi")
s=input()
compression(s)
