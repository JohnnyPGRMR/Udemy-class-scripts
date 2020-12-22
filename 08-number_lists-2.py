empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

# Sorted takes in a list and creates another list.
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# A list of characters is output as a list of strings using sorted, or you can use the "list" command to create a list from an object..
digits = list("432985617")
print(digits)

# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()
print(more_numbers)
# output below means the two lists are not the same list.
print(numbers is more_numbers)
# output below shows that they are the same list.
print(numbers == more_numbers)