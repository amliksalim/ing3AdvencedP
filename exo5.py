print("Runner 1:")
nom1=input("Name:")
time1=float(input("Time (in seconds):"))
print("Runner 2:")
nom2=input("Name:")
time2=float(input("Time (in seconds):"))

if time1<time2:
    print("The faster runner is "+nom2)
elif time1>time2:
    print("The faster runner is "+nom1)
else :
    print(nom1+" and "+nom2+" have the same time")

