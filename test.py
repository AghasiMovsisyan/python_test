'''

num = int(input('Enetr a Number'))

print(num * '9')

'''

'''

year = int(input('Enter a Number: '))

if year % 4 != 0 :
    print('No Hasarak')
elif year % 4 == 0 and year % 100 != 0:
    print('Yes Nnahanj')
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print('Yes Nahanj')
else:
    print('NO Hasarak')
'''

'''
a = int(input('Enter a NUmber: '))
b = int(input('Enter a NUmber: '))
c = int(input('Enter a NUmber: '))


if a >= c and a >= b:
    a, c =c, a
elif b >= c and b >= a:
    b, c = c, b


if c >= a + b or b >= a + c or a >= c + b:
    print('Not a triangle')
elif c**2 == b**2 + a**2:
    print('Right triangle ')
elif c**2 < a**2 + b**2:
    print('Acute triangle')
else:
    print('Obtuse triangle')

'''

'''

num = int(input("Enter a number"))

def digit_multiplication(num):
    num = int(num)
    product = 1 
    while num > 0:
        digit = num % 10
        if digit != 0:
            product *= digit
        num //= 10
    return product


print(digit_multiplication(num))

'''

'''
a1 = int(input('Enter a Number a1: '))
a2 = int(input('Enter a Number a2: '))
n = int(input('Enter a Number n: '))

d = a2 - a1
an = a1 + d*(n - 1)

print(an)

'''


'''

year = int(input('Enter a Year: '))

century = year // 100

if year % 100 != 0:
    century += 1
print(century)

'''

'''

numbers = [int(el) for el in input('Enter a Number: ').split()]

products = []

for i in range(len(numbers) - 1 ):
    product = numbers[i] * numbers[i + 1]
    products.append(product)

print(max(products))

'''

'''


word = input('Enter a Word:  ')

if word == word[::-1]:
    print('Yes')
else:
    print('No')

'''


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

''''

words = input('Enter a NUmber: ').split()

word_italian = {}

for word in words:
    if word[-1] == 'a':
        word_italian[word] = 'f'
    elif word[-1] == 'o':
        word_italian[word] = 'm'


print(word_italian)

'''

'''

words = input().split()
S = words[0]
s = words[1]

is_suffix = False
is_prefix = False

if S[:len(s)] == s:
    is_prefix = True
if S[-len(s):] == s:
    is_suffix = True

if is_suffix and is_prefix:
    print("Both")
elif is_suffix:
    print("Suffix")
elif is_prefix:
    print("Prefix")
else:
    print("Neither")

'''

'''

num1 = [int(num) for num in input('Enter a Number: ').split()]
num2 = [int(num) for num in input('Enter a Number: ').split()]

final_list = []

if len(num1) > len(num2):
    num1, num2 = num2, num1

for num in num2:
    if num in num1:
        final_list.append(num)


if len(final_list) > 0:
    print(final_list)

'''


'''

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input('ENter'))
print(factorial(n))


'''


'''

num = int(input('Enter a Number:  '))

product = 1

for i in range(2, num + 1):
    product = i * product


print(product)

'''

'''


word = input('Enter a Word: ')

def check_uppper(value):

    return value == value.upper()

if check_uppper(word):
    print('Yes')
else:
    print('No')

'''


'''
numbers = [int(elem) for elem in input('Enter a Number: ').split()]

is_ascending = False
is_descending = False


for i in range(len(numbers) - 1):
    if numbers[i] >= numbers[i + 1]:
        is_descending = True
    elif numbers[i] <= numbers[i + 1]:
        is_ascending = True


if is_ascending:
    print("Ascending")
elif is_descending:
    print("Descending")
else:
    print("Neither")

'''


'''

def bubble_sort(num):
    is_swapped = True

    while is_swapped :
        is_swapped = False
        for i in range(len(num) - 1):
             if num[i] >= num[i + 1]:
                 num[i], num[i + 1] = num[i + 1], num[i]
                 is_swapped = True

    return num


num = [int(el) for el in input('Enter a Num: ').split()]
print(bubble_sort(num))

'''

'''

def selection_sort(nums):
    for i in range(len(nums) - 1):
        minimal_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minimal_index]:
                minimal_index = j
        nums[i], nums[minimal_index] = nums[minimal_index], nums[i]

    return nums

nums = [int(el) for  el in input('Enter a Num: ').split()]
print(selection_sort(nums))


'''

'''

def binary_search(numbers,target,start,end):
    if start >= end:
        return False

    mid = (end + start)//2
    if numbers[mid] == target:
        return True
    if numbers[mid] > target:
        return binary_search(numbers,target,start,mid)
    return binary_search(numbers,target,mid + 1,end)

print(binary_search([2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37], target=37, start=0, end=16))

'''

'''
def sum_of_elements(I):
    if not I:
        return 0
    return I[0] + sum_of_elements(I[1:])


print(sum_of_elements([1,2,8,9,7,4,5]))


'''


'''


def print_reverse(n):
    if not n: 
        return         
    num = int(input())  
    print_reverse(n - 1)  
    print(num) 


n = int(input())
print_reverse(n)


'''



#Bishop


'''

def input_matrix(n):
    mat = []
    position = (0, 0)
    for _ in range(n):
        mat.append(input().split())
    return mat


def output_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print()


def find_B(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == "B":
                return i, j


def transform(mat, dirs, B_pos):
    x = dirs[0]
    y = dirs[1]
    n = len(mat)
    while 0 <= B_pos[0] + x < n and 0 <= B_pos[1] + y < n:
        mat[B_pos[0] + x][B_pos[1] + y] = "x"
        B_pos = B_pos[0] + x, B_pos[1] + y


n = 8
mat = input_matrix(8)
position = find_B(mat)
directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

for d in directions:
    transform(mat, d, position)
output_matrix(mat)


'''

#
#def is_largest(num):
 #   is_largest = True
#
 #   while num > 9 :
  #      a = num % 10
   #     b = num // 10 % 10

    #    if a > b :
     #       is_largest = False
      #      break
#
       # num = num // 10

 #   return not is_largest

#number = int(input('Enter a Number: '))
#if is_largest(number):
  #  print('Yes')
#else:
 #print('No')

'''

def is_lucky(num):
    odd_sum = 0
    even_sum = 0
    is_even = True

    for digit in num:
        if is_even:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

        is_even = not is_even

    return even_sum == odd_sum

numbers = input('Enter a Number: ')
print(is_lucky(numbers))

'''

#
# words = input('Enter a Word: ').split()
# italian_wods = {}
#
# for word in words:
#     if word[-1] == 'a':
#         italian_wods[word] = 'f'
#     elif word[-1] == 'o':
#         italian_wods[word] = 'm'
#
#
# print(italian_wods)
#
#
#
#
# num1 = [int(num) for num in input('Enetr a number:').split()]
# num2 = [int(num) for num in input('Enetr a number:').split()]
# final_list = []
#
#
# if len(num1) > len(num2):
#     num1 , num2 = num2, num1
# for num in num2:
#     if num in num1:
#         final_list.append(num)
#
# print(final_list)
#
#

#
# numbers = [int(num) for num in input('Entera a Number: ').split()]
# is_discending = False
# is_Acsending = False
#
#
#
# for i in range(len(numbers) - 1):
#     if numbers[i] >= numbers[i + 1]:
#         is_Acsending = True
#     if numbers[i] <= numbers[i + 1]:
#         is_discending = True
#
#
# if is_Acsending:
#     print('Discending')
# elif is_discending:
#     print('Acdending')
#


# import re
#
# string = 'Asjadfiou124 wnb24 b234 23 n'
# pattern = '\d+'
#
# result = re.findall(pattern, string)
# # print(result)
#




# def missing_number(values):
#     n = len(values) + 1
#     return (n * (n + 1) // 2) - sum(values)
#
# numbers = [int(i) for i in input('Enter a Numbers: ').split()]
# print(missing_number(numbers))
#


# def char_count(value):
#     dic = {}
#
#     for char in value:
#         if char not in dic:
#             dic[char] = 1
#         else:
#             dic[char] += 1
#
#     return dic
#
# print(char_count(input('ENtera a Text: ')))
#
#
#



def is_palindrome(text):
    if len(text) == 0 or len(text) == 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])



if is_palindrome((input('Enter a text: '))):
    print('Yes')
else:
    print('No')








