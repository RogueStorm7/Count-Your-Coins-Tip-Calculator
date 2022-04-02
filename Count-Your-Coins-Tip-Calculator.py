print('Welcome to Count Your Coins Tip Calculator!!!')

#asks user what the tab total is
total_tab = float(input('What is the total bill?\n'))
sales_tax = .06 
# this will get me the taxed tab amount
taxed_tab = (total_tab * sales_tax) + total_tab
# tip_percentage = .20
tip = float(input('How much tip would you like to give?'))
#how many people will you be splitting the bill with?
#prompt of what the tip will be?
tip_total = taxed_tab * (tip / 100) 
print(sales_tax)
print()
print ("How was the service? Please use good or bad.")
service = input()
# this is the grand total
grand_total = taxed_tab + tip_total 

# this is how many people are splitting the bill
num = float(input('How many people to split the bill?\n'))
tab_per_person = grand_total/ num

# tip percentage divided by 100
# tip_percentage = tip / 100

# total_tip = total_tab * tip_percentage
# total_tab = total_tab + tip

print(f"The tip will be {tip} % taxes included")
print(f"Here is your grand total: ${grand_total: ,.2f}\nEach person should pay: ${tab_per_person: ,.2f}.\nThank you for using Count Your Coins Tip Calculator!!!!")
