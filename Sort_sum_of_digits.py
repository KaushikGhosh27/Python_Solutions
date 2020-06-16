def sum_of_digits(n):
    sum=0
    num=n
    while(n!=0):
        n1=n%10
        sum=sum+n1
        n=n//10
    return num,sum

mylist=[]
newlist=[]
n=int(input("Enter no. of elemnets you want to enter: "))
for i in range(n):
    ele=int(input("Enter a number: "))
    mylist.append(ele)

print("\nOriginal List: ")
print(*mylist,sep=",")

for i in mylist:
    q=sum_of_digits(i)
    newlist.append(q)


newlist.sort()
print("\nList sorted according to sum of digits: ")
print(*newlist,sep=",")
print("List format: (entered number,sum of digits of the number)")
