def sum_of_digits(n):
    sum=0

    while(n!=0):    #1st loop     #2nd loop          #3rd loop
        n1=n%10 #123%10=3 n1=3      n=12, 12%10=2    n=1, 1%10=1
        sum=sum+n1  #sum=3          sum=3+2=5       sum=5+1=6
        n=n//10  #n=12              #n=1            #n=0

    print(sum)


sum_of_digits(574790)
