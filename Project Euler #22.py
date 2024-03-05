# Project Euler 22

f = open('names.txt', 'r')
file = f.readlines()

total = 0

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alph = {}
for n, letter in enumerate(letters):
    alph[letter] = n + 1

names = (file[0].strip()).split(',')
name_list = []
for item in names:
    string = ''
    for letter in item:
        if letter != '"' and letter != ' ' and letter != ',':
            string += letter.lower()
    name_list.append(string)

name_list = sorted(name_list)

for name in name_list:
    name_sum = 0
    for letter in name:
        name_sum += alph[letter] 
    total += name_sum * (name_list.index(name) + 1)
    
print(total)