pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2,3,4.5,8.7,3.1,9.2,1.6]
sorted_number = sorted(numbers)
print(sorted_number)
# sorted creates a new list, so original list is still present as evidenced below.
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)