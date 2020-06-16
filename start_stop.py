def counter(start,stop):
    string = ""
    if start>stop: #10,1
        string += "Counting down: "
        for i in range(start,stop,-1):
            string += "{},".format(i)
        string+= "{}".format(stop)

    elif start<stop: #1,10
        string += "Counting up: "
        for i in range(start,stop):
            string += "{},".format(i)
        string += "{}".format(stop)
    else: #56 = 56
        string+= "Counting up: {}".format(start)

    return string



for i in range(3):
    start = int(input("Enter Start: "))
    stop = int(input("Enter Stop: "))
    print(counter(start,stop))
    print()
