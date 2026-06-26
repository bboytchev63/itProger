# def test_func(a, b):
#     """
#     a: value 1
#     b: value 2

#     returns : int    
#     """
#     return a + b
# print(test_func(5,1))

# print("This prints function definition !!!")
# help(test_func)

### range
# rng = range(2, 10, 2)
# print(list(rng))


### Map
# strings = ["my", "world", "apple", "pear"]

# lengths = map(len, strings)
# print(list(lengths))

### Filter

def longer_than_4(string):
    return len(string) > 4

strings = ["my", "world", "apple", "pear"]
filtered = filter(longer_than_4, strings)
print(list(filtered))