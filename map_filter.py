# https://youtu.be/j6FCewxjrBM?t=368

num_list = [1, 2, 3, 4, 5]
# Using map function to square each element in the list
squared_list = list(map(lambda x: x * x, num_list))
print("Squared list:", squared_list)  # Output: [1, 4, 9, 16, 25]

# Why use map instead of a loop?
# It’s shorter, more expressive, and fits functional programming patterns.

# #Loop version:
# squared_list = []
# for x in num_list:
#     squared_list.append(x * x)

# # List comprehension version:   
# squared_list = [x * x for x in num_list]

filtered_list = list(filter(lambda x: x % 2 == 0, num_list))
print("Filtered list:",filtered_list)  # Output: [2, 4]




