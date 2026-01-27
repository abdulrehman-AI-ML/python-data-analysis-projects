
# ----Inputs we need from the user
# Total rent
rent = int(input("Enter the hostal rent: "))
# Total food ordered for snacking
food = int(input("Enter the amount of food orderad : "))
# Electricity units spend
electricity_Spend  = int(input("Enter the total of electricity spend: "))
# Charge per unit
charge_per_unit = int(input("Enter the charge per unit: "))
#No of persons
persons = int(input("Enter the number of persons living in room: "))
#Total Bill
total_bill = electricity_Spend * charge_per_unit

#OutPut

#Calculating the total amount each person has to pay
output = (food + rent + total_bill)//persons

#Total amount you've to pay is 

print('Each person will pay = ',output)