#1
'''

a1 = int(input("PLease enter the first digit"))
a2 = int(input("PLease enter the second digit"))
n = int(input("Enter the number of digit"))

d = a2 - a1
an = a1 + d*(n-1)
print(f '[{n}] = {an}')

'''

#2
''''
year = int(input("enter a  year "))

century = year // 100

if year % 100 != 0:
    century += 1
print(century)
'''

#3

 #variant 1
''' 
numbers = [int(el) for el in input(" Enter the sequence: ").split(" ")]

products = []                                         #for i in range(len(numbers)):
                                                     #   numbers[i] = int(numbers[i])
for i in range(len(numbers) - 1):
   product = numbers[i] * numbers[i + 1]
    products.append(product)

print(max(products))
'''
#variant 2
''''
numbers = [int(el) for el in input('Enter a Number: ').split(' ')]

max_product = numbers[0] * numbers[1]

for i in range(1, len(numbers) - 1):
    if numbers[i] * numbers[i + 1] > max_product:
       max_product  = numbers[i] * numbers[ i + 1]

print(max_product)
'''
#4

'''
number = input(" Enter a number: ")

length = len(number)
half = length // 2
sum_1 = sum_2 = 0

for i in number[:half]:
    sum_1 += int(number[i])

for i in number[half:]:
    sum_2 += int(number[i])

if sum_1 == sum_2:
    print("Yes")
else:
    print("No") 
    '''

#5
'''
word = input(' Enter a word: ')

if word == word[::-1]:
    print('yes')
else:
    print('NO')

'''

