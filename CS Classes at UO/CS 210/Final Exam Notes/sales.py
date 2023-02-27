def findRange(salesli):

    salesli.sort()
    low = salesli[0]
    high = salesli[-1]
    return low, high

def salesReport(salesli):

    low, high = findRange(salesli)
    print(f'Weekly Range: $ {low * 100} - ${high*100}\n')

    fw = 12
    print(f"{'Mon':<{fw}} {'Tue':<{fw}} {'Wed':<{fw}} {'Thu':<{fw}} {'Fri':<{fw}}")

    for sales in salesli:
        print(f'${(sales*100):<{fw}}' , end='')

    return None
