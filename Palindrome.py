def palindrome(string):
    mid=int(len(string)/2)
    first_part=string[:mid]
    temp= string[::-1] #reversing the string
    second_part=temp[:mid]
    if first_part == second_part:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

n=str(input("Enter a string: ").lower())
palindrome(n)
