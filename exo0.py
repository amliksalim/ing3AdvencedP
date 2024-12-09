n=int(input("How many people need a ride"))
x=int(input("Ask the user how many people can fit in one taxi"))

if (x%n) != 0 :
    print("number of taxis neede is :"+str((n//x)+1))