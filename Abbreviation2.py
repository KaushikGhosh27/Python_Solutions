def abbreviation(name):
    original_name = name[:]
    
    surname = name[::-1]
    surn = ''
    for i in range(len(surname)):
        surn += surname[i]
        if surname[i]==' ':
            break
    sname = surn[::-1]
    #print(sname)
    del surname
    
    


    name = name.replace(sname,"").strip()
    abv =''


    for i in range(len(name)):
        if (i == 0 or name[i-1] == ' '):
            abv += name[i].upper()+"."
    #print(abv)



    abv = abv+sname
    return abv
    #print(abv)
##
##    dic ={}
##
##    dic[original_name] = abv
##
##    return(dic)
##    


##def store_abv(name):
##
##    abv = abbreviation(name)
##
##    abv_book = {}
##
##    abv_book[name] = abv
##
##    return abv_book



n = int(input("Enter no. of names you would like to enter: "))

abv_book ={}
for i in range(n):
    name = input("Enter name: ").strip()
    abv_book[name] = abbreviation(name)
    
print()

for i,j in abv_book.items():
    print("Name: {:<30s}  {:<5s} {:>5s}".format(i,"Abbreviation:",j))


    # < to end two columns at the same place
    #> to start two columns at the same place

    
    
