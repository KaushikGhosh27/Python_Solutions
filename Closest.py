def closest(k):
    arr=[]
    temp=[]
    n=int(input("Enter the no. of elements you would like to enter: "))
    for i in range(n):
        n=float(input("Enter elements: "))
        arr.append(n)

    print(arr)

    for i in arr:
        diff= abs(k-i)
        temp.append(diff)
    #print(temp)

    minimum = temp.index(min(temp)) #the min index corresponds to the number closest to the list
    q=arr[minimum:minimum+1]
    print(str(*q)+" is the closest element to "+str(k))

print("Given a list of numbers and a variable K, where K is also a number, write a Python program to find the number in a list which is closest to the given number K.")
print()
k=float(input("Enter the element K : "))
closest(k)
        

#eg:[12,9,10]
#abs(7-12)=5
#abs(7-9)=2
#abs(7-10)=3
#2 is minimum
#[5,2,3]
#index of 2 is 1
#therefore print the index which corresponds to the lowest element. Therefore, 1st index of arr is 9 which will be the lowest number
