#1
'''
#
# def missing_number(values):
#     n = len(values) + 1
#
#     full_sum = int(n * (n + 1) / 2)
#
#     return full_sum - sum(values)
#
# numbers = [int(i) for i in input('Enter a Numbers: ').split()]
# print(missing_number(numbers))

def missing_number(values):
    n = len(values) + 1
    return (n * (n + 1) // 2) - sum(values)

numbers = [int(i) for i in input('Enter a Numbers: ').split()]
print(missing_number(numbers))


'''

#2


'''

def segment_length(x1, x2, y1, y2):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2 ) ** 0.5
    return distance


def perimeter(values):
    p = segment_length(values[0], values[1], values[2], values[3])
    p += segment_length(values[2], values[3], values[4], values[5])
    p += segment_length(values[4], values[5], values[6], values[7])
    p += segment_length(values[6], values[7], values[0], values[1])

    return p


coords = [float(i) for i in input('Enter a sequence: ').split()]
print(perimeter(coords))

'''

























