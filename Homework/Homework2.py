#1

#variant 1

'''
word = input('Enter some text: ')

def check_upper_1(value):
    return value == value.upper()
if check_upper_1(word):
        print('Yes')
else:
        print('No')


#variant 2

print('Yes' if word.isupper() else 'No')

'''

#2

#varianti

#
# def digit_sum(num):
#     _digit_sum = 0
#
#     while num > 0:
#         _digit_sum += num % 10
#         num //= 10
#
#     return _digit_sum
#
# def number_root(num):
#     while num > 9:
#         num = digit_sum(num)
#
#     return num
#
#
# # num = int(input('Enter a number: '))
# print(number_root(num))
#


#variant 2


'''

def number_root(number):
    sum = 0
    while  number != 0:
        digit = number % 10
        sum += digit
        number //= 10

    if sum < 10:
        return sum
    else:
        return number_root(sum)

number = int(input('Enter a number'))
print(number_root(number))

'''

#3
'''
def is_largest(value):
    is_largest = True

    while value > 9:
        a = value % 10 
        b = value // 10 % 10 

        if a > b:
            is_largest = False
            break

        value = value // 10 

    return not is_largest

number = int(input('Enter a number: '))
if is_largest(number):

    print('Yes')
else:
    print('NO')

'''

#4
'''

#variant1

def is_lucky(value):
    odd_sum = 0
    even_sum = 0
    is_even = True

    for digit in value:
        if is_even:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

        is_even = not is_even

    return even_sum == odd_sum

num = input('Ener a number: ')
print(is_lucky(num))

'''

#variant2
'''


def is_Lucky(value):
    lucky_sum = 0

    for digit in value[0::2]:
        lucky_sum = lucky_sum + int(digit)

    for digit in value[1::2]:
        lucky_sum = lucky_sum - int(digit)

    return  lucky_sum == 0


'''

#5

'''

def stools(values):
    max_height = max(values)
    result = 0

    for height in values:
         result += max_height - height

    return result

    #return sum([max_height - height for height in values])

#heights = list(map(int, input('Enter a sequence').split()))
heights = [int(i) for i in input('Enter a sequence: ').split()]
print(stools(heights))

'''



#6
'''

def is_prime(value):
    _is_prime = True

    for i in range(2, value // 2 + 1):
        if value % i == 0:
            _is_prime = False
            break

    return _is_prime


def goldbach(value):
    for i in range(2, value):
        if is_prime(i) and is_prime(value - i):
            return i, value - i


num = int(input('Enter a Number: '))
prime1 , prime2 = goldbach(num)

'''
