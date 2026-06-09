# https://www.youtube.com/watch?v=GWZf_B129zs


# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# # for value in my_generator():
# #     print(value)
# # # Output:

# gen_values = my_generator()
# # print(next(gen_values))  # Output: 1    
# # print(next(gen_values))  # Output: 2
# # print(next(gen_values))  # Output: 3
# # # print(next(gen_values))  # This will raise StopIteration since there are no more values to yield

# for value in gen_values:
#     print(value)
# # OR
# for value in my_generator():
#     print(value)



# # Get Prime Numbers not using Generator
# def Get_Primes_List(start,end):
#     primes = []
#     for num in range(start, end + 1):
#         if num > 1:
#             for i in range(2, int(num**0.5) + 1):
#                 if (num % i) == 0:
#                     break
#             else:
#                 primes.append(num)  
#     return primes

# Get_Primes_List(1, 100)  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
# print(Get_Primes_List(1, 100))
# print(Get_Primes_List(1000, 1100)) # Output: [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097]

# Get Prime Numbers using Generator
def Get_Primes(start,end):
    for num in range(start, end + 1):
        if num > 1:
            is_prime = True  # Assume the number is prime until proven otherwise
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    is_prime = False    
                    break
            if is_prime:
                yield num  # Yield the prime number instead of appending to a list
                is_prime = True  # Reset is_prime for the next iteration

    

# for prime in Get_Primes(, ):
for prime in Get_Primes(50, 100):
    print(prime)

# for prim ending with 7
for prime in Get_Primes(1, 100):
    if str(prime).endswith('7'):
        print(prime)

# or
for prime in Get_Primes(1, 100):
    if prime % 10 == 7:
        print(prime)

# which is faster?
import time
pp = []
start_time = time.time()
for prime in Get_Primes(1, 100):
    if prime % 10 == 7:
        pp.append(prime)
end_time = time.time()
print(f"Execution time when checking last digit : {end_time - start_time} seconds")

pp=[]
start_time = time.time()
for prime in Get_Primes(1, 100):
    if str(prime).endswith('7'):
        pp.append(prime)
end_time = time.time()
print(f"Execution time when using endswith : {end_time - start_time} seconds")  



