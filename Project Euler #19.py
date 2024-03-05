# Project Euler 19

total = 0
months = ['January', 'Febrary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
successive_days = [1]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_dict = {}

for n, month in enumerate(months):
    month_dict[month] = days_in_month[n]

def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False

day = 0
for year in range(1900, 2001):
    if is_leap_year(year):
        month_dict['Febrary'] = 29
    else:
        month_dict['Febrary'] = 28
        
    for month in month_dict:
        for i in range(1, month_dict[month] + 1):
            if day > 6:
                day = 0
            
            if i == 1 and days[day] == 'Sunday' and year != 1900:
                total += 1
            day += 1

print(total)