# # List Comprehensions - Visually Explained

# nums = [1,2,3,4,5]
# nums_squared = []
# nums_squared = []
# for n in nums:
#     square = n ** 2
#     nums_squared.append(square)
# print('Using For Loop :', nums_squared)

# nums_squared = [n**2 for n in nums]
# print('Using List Comprehension :',nums_squared)

# print('#################################################')
# tv_shows = ["friends", "PARKS AND RECREATION","the Office", "30 rock", "modern FAMILY"]
# tv_shows_cap = []
# for show in tv_shows:
#     show_cap = show.title()
#     tv_shows_cap.append(show_cap)
# print(tv_shows_cap)

# tv_shows_cap.clear
# tv_shows_cap = [ show.title() for show in tv_shows_cap]
# print('List compprehensive  ',tv_shows_cap)

# tv_shows_cap.clear
# tv_shows_cap = [show.title() for show in tv_shows_cap if len(show) >= 10]
# print('List compprehensive using <if>  ',tv_shows_cap)
################## Faster #######################################
from time import time
start = time()
n = [n**2 for n in range(1,30000001)]
end = time()
print('List comp run time ',end-start)

start = time()
squares = []
for n in range(1, 30000001):
    squares.append(n ** 2)
end = time()
print("Loop + append run time:", end - start)