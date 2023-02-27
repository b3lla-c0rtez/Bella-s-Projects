'''
More Automated Testing and Debugging
CIS 210 Project 6-2 Winter 2021Functions need to be tested and debugged;
write a function to automate testing of calendar function (project 5-1)
'''

import doctest

def bigSalesBug(sales_list):
    '''(list) -> number

    Returns sum of all sales for amounts at or over $40,000.
    sales_list has the record of all the sales.

    >>> bigSalesBug([40_000, 45.67, 19_000.0, 25000, 100_000])
    140000.0
    '''

    total = 0.00
    for sales in sales_list:
        if sales > 40_000:
            tottal = total + sales
        
        return total

def findRangeBug(salesli):
    '''(list) -> tuple
    Returns largest and smallest number in non-empty salesli.
    (Note that Python has built in funcs max and min
    to do this, but not using them here, so we can
    work with the list directly.)
    >>> findRangeBug([40000, 45.67, 19000.0, 25000, 100000])
    (45.67, 100000.0)
    '''

    salesli = salesli.sort()
    low = float(salesli[0])
    high = float(salesli[-1])
    return low, high

def salesReportBug(salesli):
    '''(list) --> None

    Prints report of sales totals for each day of week (salesli)
    and range of per-day sales. salesli is non-empty - 0 sales
    for any day are reported as 0.

    >>> salesReportBug([40000, 45.67, 19000.0, 25000, 100000])
    Weekly Range: $45.67 - $100,000.00
    Mon          Tue          Wed          Thu          Fri
    $40,000.00   $45.67       $19,000.00   $25,000.00   $100,000.00      '''

    # calculate and report low and high sales
    low, high = findRangeBug(salesli)
    print(f'Weekly Range: ${low:,.2f} - ${high:,.2f}\n')
    
    # print daily report header
    fw = 12
    print(f"{'Mon':<{fw}} {'Tue':<{fw}} {'Wed':<{fw}} {'Thu':<{fw}} {'Fri':<{fw}}")
    
    # report on sales per day from list data
    for sales in salesli:
        print(f'${float(sales):<{fw},.2f}', end='')
    return None

print(doctest.testmod())
