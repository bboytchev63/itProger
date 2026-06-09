# Python Lambda Functions
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.

# def squire(x):
#     return x * x

# def cube(x):
#     return x * x * x

# def transform_list(lst, func):
#     return [func(x) for x in lst]


# print(transform_list([2,3], squire))  # Output: 4, 9
# print(transform_list([2,3], cube))  # Output: 8, 27


# Use      Lambda functions

def transform_list(numlist, transform_func):
    return [transform_func(x) for x in numlist]

print(transform_list([2,3], lambda x: x * x))  # Output: 4, 9
print(transform_list([2,3], lambda x: x * x * x))  # Output: 8, 27



