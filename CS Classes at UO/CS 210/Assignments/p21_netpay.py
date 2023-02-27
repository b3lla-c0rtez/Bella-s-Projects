'''
Calculate Netpay: Netpay.CIS 210 Project 2-1 Netpay Assignment
Author: Isabella Cortez
Credits: Austin Vierra, Lauren Mathews
Calculate the netpay based off of tax rate, pay rate, work hours, and hourly wage
'''

def tax(gross_pay): # function header
    
    '''
    (int) -> float

    Takes an integer, which is the
    gross and returns the pay rate.
    It returns the pay rate based
    on the tax rate which is .15.
    The tax and gross are multiplied
    to get the pay rate.
                        #Examples of Use
    >>>tax(1)
    0.15
    >>>tax(40)
    6.0
    '''
    
    tax_rate = .15
    pay_rate = tax_rate * gross_pay
    return pay_rate

def netpay(work_hours): # function header
    
    '''
    (int) -> float

    Takes an integer, which is the
    hours and figures out the gross
    price based on the hours of work
    and pay rate per hour. The pay
    rate per hour is 11.25. The cost
    does the tax function on the gross
    pay. Then the total answer is
    the cost subtracted from the cost
    and it is rounded to two decimal
    points.
                        #Examples of Use
    >>>netpay(1)
    9.56
    >>>tax(40)
    382.5
    '''
    
    hourly_rate = 11.25
    gross_pay = work_hours * hourly_rate
    cost_tax = tax(gross_pay)
    answer = round(gross_pay-cost_tax, 2)
    return answer

def main(): # function header
    
    '''
    () -> None
    
    Net pay for program driver.
    '''
    
    print('For 1 hours work, netpay is: ' , netpay(1))
    print('For 40 hours work, netpay is: ' , netpay(40))
    return None

main()
