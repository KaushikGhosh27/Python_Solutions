mylist=[]
n=int(input("Enter the no.of elements you would like to enter: "))
for i in range(n):
    ele=int(input("Enter a number: "))
    mylist.append(ele)
minimum = mylist[:1]
for i in mylist:
            for j in mylist:
                if i<j:
                    minimum = i
print(minimum)
                    
    
