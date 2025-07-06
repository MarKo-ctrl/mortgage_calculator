#!/usr/bin/env python

welcome_message = '''
    Welcome to Mortgage Calculator!
    Here you can calcullate the monthly payment of a mortgage,
    or the term required to repay that mortage for a fixed monthly payment.
    
    First, I need to ask a few questions:
''' 

def print_prompt(prompt):
    print(prompt)

if __name__ == "__main__":
    print_prompt(welcome_message)