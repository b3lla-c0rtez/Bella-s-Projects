##def my_in(li, i):
##    for item in li:
##        return item == i
##    return -1

def createTempD():
    days = ['Mo','Tu','We','Th']
    temps = [55, 23, 42, 44]

    temperature = int(input("Enter temp: "))
    temps.insert(4, temperature)

    while len(temps) <= 6:
    
        day = input("Enter day: ")

        if day == 'mo' or day == 'monday':
            print(temps[0])

        if day == 'tu' or day == 'tuesday':
            print(temps[1])

        if day == 'we' or day == 'wednesday':
            print(temps[2])

        if day == 'th' or day == 'thursday':
            print(temps[2])
            
        if day == 'fr' or day == 'friday':
            days.insert(4, 'Fr')
            print(temps[4])

        if day == 'sa' or day == 'saturday':
            days.insert(5, 'Sa')
            temperature = int(input("Enter temp: "))
            temps.insert(5, temperature)
            print(temps[5])

        if day == 'su' or day == 'sunday':
            days.insert(6, 'Su')
            temperature = temps[5] + 10
            temps.insert(6, temperature)
            print(temps[6])
