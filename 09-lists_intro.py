computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

# computer_parts[3] = "trackball"
print(computer_parts[3:])

# Adding square brackets converts "trackball" from a string to a string that is part of a list.
# which allows the colon operator to swap out multiple items in the target list for the desired insertion.
computer_parts[3:] = ["trackball"]
print(computer_parts)