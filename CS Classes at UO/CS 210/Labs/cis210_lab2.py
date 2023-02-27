def is_even(n):
    '''
    (int) -> boolean
    
    Returns true if n
    is an even number.

    >>>is_even(100)
    True
    >>>is_even(101)
    False
    >>>is_even(0)
    True
    '''
    print('in function is_even')
    return (n % 2) == 0

print(is_even(2))
result = is_even(3)

def welcome():
    '''
    () -> ()

    Print welcome message

    >>> welcome()
    Good morning, CIS 210!
    print('Good morning, CIS 210!')
    return None
    '''
    print('Good morning, CIS 210!')
    return None
welcome()
    
def est_tax(income, exemptions):
    '''
    (number, integer) -> float
    Geberates an estimate for federal income tax.
    Prints result.
    Example from class revised to print (not return) estimated tax.

    >>> est_tax(20000, 1)
    1870.0
    '''
    
    # set values needed to generate estimate
    std_exempt = 4150
    std_deduct = 6500
    tax_rate = .20

    # calculate federal tax by adjusting
    # reported income and applying tax rate
    taxable_income = income - std_deduct
    exempt_adjust = std_exempt * exemptions
    taxable_income = taxable_income - exempt_adjust
    estimated_tax = taxable_income * tax_rate

    print('Estimated tax is' , estimated_tax)
    return None
est_tax(20000, 1)

def est_tax2(income2, exemptions2):
    '''
    (number, int) -> float
    
    Generates an estimate for federal income tax.
    
    CALLS: taxable

    >>> est_tax2(20000, 1)
    1870.0
    '''

    std_exempt2 = 4150
    std_deduct2 = 6560
    tax_rate2 = .20

    taxable_income2 = taxable(income2, exemptions2, std_exempt2, std_deduct2)
    estimated_tax2 = taxable_income2 * tax_rate2
    print('Estimated tax is:' , estimated_tax2)
    return None

def taxable(income2, exemptions2, std_exempt2, std_deduct2):
    '''
    (number, int, number, number)
    Adjust gross income (i) to taxable income
    by applying standard deduction and exemptions.

    Called by: est_tax

    >>>taxable(20000, 1, 4150, 6500)
    9350
    '''

    taxable_income2 = income2 - std_deduct2
    exempt_adjust = std_exempt2 * exemptions2
    taxable_income2 = taxable_income2 - exempt_adjust

    return taxable_income2

est_tax2(20000, 1)
