shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))

# Line 16 with the chained assignments is equivalent to 
# line 17 + with the individual assignments, i.e. a = another_list, b = another_list, etc.
a = b = c = d = e = f = another_list
print(a)

print("Adding cream")   # Adding a print result to make it easier to find out what is going on.
b.append("cream")  # calling method append to add cream to the list.
print(c)
print(d)

