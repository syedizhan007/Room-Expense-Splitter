## inputs we need from the user
#total rent
#total food ordered for snacking
#elactricity units spend 
#charg per unit
#persons living in room/flat

rent = int(input("enter your flat rent:"))
food = int(input("enter your amount of food ordered:"))
elactricity_spend =int(input("enter the total of elactricity_spend"))
charg_per_unit =int(input("enter thr charg per unit:"))
person = int(input("enter the number of persons living in room/flat "))

total_bill = elactricity_spend * charg_per_unit
total_bill = food + rent

output = total_bill / person
print("this is total bill=",total_bill)
print("each person bill =", output)
