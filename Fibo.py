def fibo(n):

    first_no = 0
    second_no = 1
    l=[0,1]

    if n==0:
        print("Error.Enter no. greater than zero")

    elif n==1:
        print("The first term of Fibbonaci series:",[0])

    elif n>1:

        for i in range(n-2):  # Since 0 and 1 are already included in the list so we run the loop two times less than n.
            x=first_no +second_no
            l.append(x)
            first_no=second_no
            second_no=x
    
        print("The first ",str(n),"terms of Fibonacci numbers are: ",l)


n=int(input("Enter the no. of terms: "))
fibo(n)


