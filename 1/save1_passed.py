def sum_numbers(numbers=None):
    if numbers == None:
        return sum([x for x in range(101)])
    else:
        return sum([x for x in numbers])
