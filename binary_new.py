def binary(n):
    string = ""
    while n!=0:
        n1 = int(n%2)
        string+= "{}".format(n1)
        n = int(n/2)

    decimal  = (string[::-1])

    return decimal

    #print(type(decimal))
    


num = int(input())
dec = binary(num)
temp_count = 1
actual_count = 0
#print(dec)

#dec = '111001110'
#dec = '101'
for i in range(len(dec)-1):
    if dec[i] == dec[i+1] == '1': #dec is a string , hence we must use string 1 and not int 1
        temp_count = temp_count+1
        if temp_count>actual:
            actual_count = temp_count
    else:
        temp_count = 1

if actual_count != 0:
    print(actual_count) # if there is any change in actual that means at least 1 pair of consecutive 1's exist
else:
    print(1) #if actual still remains 0 at the end of program means the max no of consecutive 1 is 1
                #eg dec = '101' : actual will never change since if condition will never be satisfied.

