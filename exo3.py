
montant_total=float(input("total amount: "))
nbr_item=int(input("Number of items: "))
jour=input("Day of the week:")

if jour.lower()=="saturday" or jour.lower()=="sunday":
    montant_total_after_disc=montant_total-montant_total*0.2
    if nbr_item>5 :
        montant_total_after_disc=montant_total_after_disc-montant_total_after_disc*0.05

else :
     montant_total_after_disc=montant_total-montant_total*0.1


print("Total amount"+str(montant_total))
print("Number of items:"+str(nbr_item))
print("Day of the week:"+jour)
print("Total price after discount: "+str(montant_total_after_disc))
