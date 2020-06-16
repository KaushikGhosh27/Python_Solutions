def ss(string,substring):
    sublen=len(substring)
    count=0
    for i in range(len(string)-((len(substring))+1)):   
        if string[i:i+sublen]== substring:  
            count+=1
       
    print(count)



ss("zebebra","eb")

 #zebra=5(index=4)
  #eb=2
  # 1) loop needs to run till 3rd index because we need to check the last 2(3rd,4th index)
  #    index are checked as well. 
  # 2) for loop needs to check every 2 characters from beginning. Thus,
  # we write i:i+2.
    
  #  i=0 string[0:2]
  #  i=1 string[1:3]
  #  i=2 string[2:4]
  #  i=3 string[3:5]
    #In this case: for loop runs from 0 to 4(so that 3 is included)
    #thus we write len(substring)+1

 
