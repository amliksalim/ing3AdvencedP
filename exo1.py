name=input("please enter your name :")
if name=='VIP' :
    print("Enjoy the show for free!")

else :
    x=int(input("How many tickets would you like to buy?"))
    prix_unitaire=15.50
    print("The total cost is"+str(prix_unitaire*x))
    print("Enjoy your tickets!")
