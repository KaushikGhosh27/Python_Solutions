def c2f(c):
    return "Temperature in Farhenheit: "+str(round((((9/5)*c )+32),3))+" F"
def f2c(f):
    return "Temperature in Celcius: "+str(round(((f-32)*(5/9)),3))+" °C"
print("Choose 1 or 2\n")
print("1)To convert from Celcius to Farhenheit.")
print("2)To convert from Farhenheit to Celcius.")
n=int(input("\nEnter choice:"))
if n==1:
    c=float(input("Enter temperature in celcius: "))
    print(c2f(c))
elif n==2:
    f=float(input("Enter temperature in farhenheit: "))
    print(f2c(f))
else:
    print("Invalid choice")
    

