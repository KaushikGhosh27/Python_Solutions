def compression(s):
    count=1
    current=0
    l1=[]
    for i in range(len(s)-1):
        if s[i+1]== s[current]:
            count+=1
        else:
            print(s[current],count)
            current=i+1
            count=1
    print(s[current],count)

compression("aaabbccdefggghhi")
print()
compression("aabbccddii")
