def duplicate(array):
    new_array = []
    for i in range(len(array)):
        if array[i] not in new_array:
            new_array.append(array[i])
    if len(array) == len(new_array):
        print("No duplicate elements")
    else:
        return new_array
              
array=[]
n=int(input("Enter the no. of elements you want to enter in list: "))
for i in range(n):
    q = int(input("Enter element: ").rstrip())
    array.append(q)
print("Original array:",array)
print("After removing duplicate elements:",duplicate(array))
#print(duplicate(array))
