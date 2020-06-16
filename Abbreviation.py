name="Geeks for Geeks"
q=name.split()
#print(q)
u=""
for i in q[:(2)]:
    u=u+i[0].upper()+"."
print(u+" "+q[-1])


def abbreviation(name):
    n_split=name.split()
    abv=""
    size=len(n_split)-1
    for i in n_split[:size]:
        abv=abv+i[0].upper()+"."
    return abv+" "+n_split[-1]


name=input("Enter Name: ")
print(abbreviation(name))
