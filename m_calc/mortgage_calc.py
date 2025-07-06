#!/usr/bin/env python

welcome_message = '''
    Welcome to Mortgage Calculator!
    Here you can calcullate the monthly payment of a mortgage,
    or the term required to repay that mortage for a fixed monthly payment.
    
    First, I need to ask a few questions:
''' 

# user_principal = input('What is the mortgage amount? ')
# principal = round(float(user_principal), 2)

# user_rate = input('What is the interest rate? ')
# rate = float(user_rate)

# user_term = input('What is the term of the mortgage (in years)? ' )
# term_months = int(user_term) * 12

def monthly_payment_amount(principal, rate, term):
    """
    Calculate the monthly payment amount for a mortgage,
    on a Capital & Interest repayment schedule.

    Args:
        principal (float): The mortgage amount.
        rate (float): The interest rate.
        term (int): The term of the mortgage in years.

    Returns:
        float: The monthly payment amount.
    """
    # Calculate the monthly interest rate
    monthly_rate = (rate / 12)/100

    # Calculate the term in months
    term_months = term * 12

    # Calculate the numerator and denominator for the formula
    numerator = monthly_rate*(1+monthly_rate)**term_months
    denominator = ((1+monthly_rate)**term_months)-1

    # Calculate the monthly payment amount
    payment = principal*(numerator/denominator)

    # Round the payment to two decimal places
    return round(payment,2)

def print_prompt(prompt):
    print(prompt)

if __name__ == "__main__":
    print_prompt(welcome_message)