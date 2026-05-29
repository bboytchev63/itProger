# print("Rakia Burgas63")
# print("Rakia, 21, 'Lv'")
# print("Rakia, 21,'Lv',sep='-')")
# print("Rakia", "21", "Lv", sep="-", end="!")
# print("First line\nSecond line \n \t Third line")
# #4 – Переменные и типы данных
# print("#4 – Переменные и типы данных")
# number = 5
# print("Number = ", number)
# numberSTR = "10"
# print("NumberSTR = ", numberSTR)2
# print("Number + NumberSTR = ", number + int(numberSTR))

# #5 – Условные операторы
# print("#5 – Условные операторы")
# user_data = int(input("Enter number: "))
# if user_data > 5:
#    print("Number is bigger than 5")
#    if user_data > 10:
#          print("Number is bigger than 10")

# isHappy = True

# if isHappy:
#     print("I am happy")
# else:
#     print("I am not happy")

# data = input("Enter something: ")
# if data.isdigit():
#     print("You entered a number")
# elif data.isalpha():
#     print("You entered a string")

# #6 – Циклы и операторы в них (for, while)
# print("#6 Циклы и операторы в них (for, while)")
# for i in range(1, 5):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# count = 0 
# word = "Python"
# for i in word:
#     print(i)
#     if i == "h":
#         count += 1
# print("Count of h in Python is ", count)

# for i in range(1, 6):
#     print(i)
#     if i == 3:
#         break

# #7 – Списки (list). Функции и их методы
# print("#7  Списки (list). Функции и их методы")
# nums = [1, 2, 3, 4, 5,2,11,8]
# print(nums)
# nums[0] = True
# print(nums)
# nums.append(6)
# print(nums)

# nums2 = [7, 8, 9, 10,[True,False]]
# print(nums2)

# nums.sort()
# print(nums)

# nums.remove(2)
# print(nums)
# nums.pop(0)
# print(nums)

# nums = [1, 2, 3, 4, 5,1.5,True, "50"]
# print(nums)
# for i in nums:
#     print(i, type(i))

n = input("Enter length")
userlist = []
i = 0
while i < int(n):
    userlist.append(input("Enter element: "))
    i += 1
print(userlist)

# https://youtu.be/pqaBWcsBGyA?t=10
         
          

          