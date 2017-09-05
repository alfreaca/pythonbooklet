bank_holidays = [1, 0 , 1, 1, 2, 0, 0, 1, 0, 0, 0, 2]
month1 = int(input("Which month would you like?: "))

def bank_holiday(month) :
             return bank_holidays[month -1]
            

print(bank_holiday(month1))
    
