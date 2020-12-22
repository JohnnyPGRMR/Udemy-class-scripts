even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)
another_even = even
print(another_even)

# This sort method doesn't create a copy of the list, it rearranges the items in the list.
even.sort(reverse=True)
print(even)
# There is only one list present in this program.  Sorting it has resulted in the same list being sorted.
print(another_even)


