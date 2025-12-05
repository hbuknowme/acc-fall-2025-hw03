def get_lowest_list_value(numbers):
    # manually find the smallest number without using min()
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest


def get_highest_list_value(numbers):
    # manually find the largest number without using max()
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest