# Milo Perry 2536119
# Develop a program that accurately calculates
# dollar amount, tax, tip, and grand total for a meal at a restaurant.
    # Show user input for cost of meal as decimal amount.
    # Show user input for tip (standard tip percent) as whole number
    # Use tax rate of 7 percent (not shown), store as properly named constant
    # Calculate dollar amount of tip and tax
    # and add to original cost for grand total
    # Display tax, tip, and grand total to user.
    # Use f-string printing


cost = float(input(f'What is the total cost of the meal? $'))

tip_percent = int(input(f'What is the tip percentage? '))

tip_percent = tip_percent / 100

tip_total = cost * tip_percent

sales_tax = 0.07 # I originally tried to assign the decimal as ".07," but cotinued
                 # to get an error until I added a zero to the left of the decimal.

grand_total = cost * (1 + sales_tax) + tip_total

user_input = float(input(f'A ${cost:.2f} meal'
                         f' with a {tip_percent * 100:.0f}% tip of ${tip_total:.2f}'
                         f' and a 7% tax has a grand total cost of ${grand_total:,.2f}'))

# The below is used to show each value the input by the user.
print(user_input)


