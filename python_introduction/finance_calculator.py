#Personal finance calculator

#prompt user for financial details
monthly_income = int(input('Enter your monthly income:'))
monthly_expenses = int(input('Enter your total monthly expenses:'))

#calculate monthly savings
Monthly_Savings = monthly_income - monthly_expenses

print('Your monthly savings are', '$',Monthly_Savings)

#Projection of annual savings
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)

print('Projected savings after one year, with interest, is:', '$',Projected_Savings)

