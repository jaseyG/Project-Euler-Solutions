import calculations

number = 600851475143
tester = 3

while tester < number/2:
    if calculations.primeChecker(tester):
        if number % tester == 0:
            print(tester)
            tester += 2
        else:
            tester += 2
    else:
        tester += 2
