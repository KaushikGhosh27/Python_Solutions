def translate(n):
    caps='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    word=''
    for i in n:
        if i in caps:
            i=i.lower()
            word=word+i
        else:
            i=i.upper()
            word=word+i
    
    print("Output:",word)

print("Program to convert upper case to lower case and vice versa in a given string.")
n=str(input("Enter string: "))
translate(n)

