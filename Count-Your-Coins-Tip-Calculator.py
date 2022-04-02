print('Welcome to Count Your Coins Tip Calculator!!!')

#asks user what the tab total is
total_tab = float(input('What is the total bill?\n'))
sales_tax = .06 + total_tab
tip_percentage = .20
#prompt of what the tip will be?
tip = total_tab * tip_percentage
print(sales_tax)
print()
print(tip)
print ("How was the service? Please use good or bad.")
service = input()


tip = float(input('How much tip would you like to give?'))
#how many people will you be splitting the bill with?
num = float(input('How many people to split the bill?\n'))

#tip percentage divided by 100
tip_percentage = tip / 100

# total_tip = total_tab * tip_percentage
total_tab = total_tab + tip
tab_per_person = total_tab/ num

grand_total = "{:.2f}".format(tab_per_person)
print(f"The tip will be {tip} % taxes included")
print(f"Each person should pay: ${grand_total} Thank you for using Count Your Coins Tip Calculator!!!!")