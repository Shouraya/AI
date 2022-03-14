# This module includes the function to calculate the Compound interest.

def calculator(principleAmount, interestRate, time):
    amount = principleAmount * ((1 + ((interestRate / 100))) ** time)
    calculatedCompoundInterest = amount - principleAmount
    return calculatedCompoundInterest