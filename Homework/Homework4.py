#1
'''


def char_count(value):
    result = {}

    for char in value:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

    #for char in value:
        #result[char] = result.get(char,0) + 1


    return result

print(char_count(input('Enter a text: ')))

'''

#2

'''


def roman_to_int(value):
    romans = {'I': 1, 'V': 5 ,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

    result = romans[value[-1]]

    for i in range(len(value) - 1):
        char = value[i]
        next_char = value[i + 1]
        if romans[char] < romans[next_char]:
            result -= romans[char]
        else:
            result += romans[char]

    return result


print(roman_to_int(input('Ener a number a roman format: ')))

'''

