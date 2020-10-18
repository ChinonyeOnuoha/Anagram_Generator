data_1 = input('Enter first word :')
data_2 = input('Enter second word :')

an_anagram = sorted(data_1) == sorted(data_2)
not_an_anagram = sorted(data_1) != sorted(data_2)

print('This is an anagram :', an_anagram)
print('This is not an anagram :', not_an_anagram)
