#1
'''

num = int(input('Enter a Number: '))

print(num * '9')

'''




#2
'''

year = int(input("Enter the year"))

if year % 4 != 0:
    print("No Hasarak")
elif year % 4 == 0 and year % 100 !=0:
    print("Yes Hahanj")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("Yes Nahanj")
else:
    print("No Hasarak")
'''

#3

'''

a = int(input("Enter the number"))
b = int(input("Enter the number"))
c = int(input("Enter the number"))

if a >= b and a >= c:
    a, c = c, a
elif b >= c and b >= a:
    b, c = c, b

if a >= b + c or b >= a + c or c >= a + b:
    print(" Not a triangle ")
elif c**2 == b**2 + a**2:
   print(" Right triangle ")
elif c**2 < a**2 + b**2:
    print(" Acute triangle ")
else:
     print("Obsute triangle")
'''

#4

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