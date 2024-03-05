# Project Euler 17

digits = {'none' : 0, 1: 3, 2: 3, 3: 5, 4:4, 5:4, 6:3, 7: 5, 8:5, 9:4}
teens = {'none' : 0, 10 : 3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
tens = {'none' : 0, 20: 6, 30: 6, 40: 5, 50: 5, 60:5, 70:7, 80:6, 90:6}
# Added the extra 3 letters for 'and' that every hundred has
hundreds = {'none': 0, 100:13, 200:13, 300:15, 400: 14, 500:14, 600:13, 700:15, 800: 15, 900:14}

sum = 0

for i in range(1, 1001):
    if i < 10:
        sum += digits[i]
    elif i < 20:
        sum += teens[i]
    elif i < 100:
        if i % 10 == 0:
            sum += tens[i]
        else:
            sum += tens[int(i/10)*10] + digits[i % 10]
    elif i < 1000:
        if i % 100 == 0:
            sum += hundreds[i] - 3
        elif int((i%100) / 10) == 0:
            sum += hundreds[int(i/100)*100] + digits[i%100]
        elif int((i % 100) / 10) == 1:
            sum += hundreds[int(i/100)*100] + teens[i%100] 
        elif int(i % 100) % 10 == 0:
            sum += hundreds[int(i/100)*100] + tens[int(i%100/10)*10]
        else:
            sum += hundreds[int(i/100)*100] + tens[int(i%100/10)*10] + digits[int(i%100) - int(i%100/10)*10]
    
print(sum + 11)