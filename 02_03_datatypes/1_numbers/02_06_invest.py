'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

amount = int(input('How much will you invest?'))
interest = int(input('What\'s an interest rate?'))
years = int(input('How many years?'))

final_sum = amount + (amount * interest/100*years)
print(int(final_sum))
