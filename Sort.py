#Bubble sort

'''

def bubble_sort(nums):
    is_swapped = True
    n = len(nums)
    while is_swapped:
        is_swapped = False
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                is_swapped = True
        n -= 1
    return nums


numbers = [int(elem) for elem in input().split()]
print(bubble_sort(numbers))

'''

#Selection sort

'''

def selection_sort(nums):
    for i in range(len(nums) - 1):
        minimal_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minimal_index]:
                minimal_index = j
        nums[i], nums[minimal_index] = nums[minimal_index], nums[i]

    return nums


numbers = [int(elem) for elem in input().split()]
print(selection_sort(numbers))

'''

#Insertion sort

'''

def insertion_sort(nums):
    for i in range(len(nums)):
        values_to_items = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > values_to_items:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = values_to_items
    return nums


numbers = [int(elem) for elem in input().split()]
print(insertion_sort(numbers))

'''

