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

# n = input("Enter length")
# userlist = []
# i = 0
# while i < int(n):
#     userlist.append(input("Enter element: "))
#     i += 1
# print(userlist)

# https://youtu.be/pqaBWcsBGyA?t=10
         
# from itertools import count


# wird = "Rakia"
# print(wird[0])
# print(len(wird))
# print(wird.count('a'))
# print(wird.upper())
# print(wird.find('k'))

# word = "Rakia,wine,beer"
# print(word.split(","))
# drinks = word.split(",")

# for i in drinks:
#     print(i)

# for i in range(len(drinks)):
#     drinks[i] = drinks[i].capitalize()

# print(drinks)
# print('------------------')
# result = " and ".join(drinks)
# print(result)

# word = "Rakia-Burgas63"
# print(word[6:12])
# print(word[-2:])
# print(word[5:-3])     
# print(word[::2])     

# list1 = [1, 2, "Stroka", True, 1.5,2]
# print(list1[2])
# print(list1[-2])
# print(list1[2:])
# print(list1[::-1])

# #9 – Кортежи (tuple)
# data = (1, 22, "Stroka", True, 1.5,22)
# print(data[2])
# print(data[1:4])
# print(data[::-1])
# print(data.count(22))

# data1 = 1,2,3,"Maria",False,3.14
# print(data1)
# for i in data1:
#     print(i)

# nums = [1, 2, 3, 4, 5]
# data2 = tuple(nums)
# print(data2)

# data3 = tuple("Rakia")
# print(data3)

#10 – Словари (dict)
# data = {"name": "Rakia", "age": 21, "city": "Burgas"}
# print(data["age"])
# data["age"] = 22
# data1 = {"name": "Maria,Stoiana", "age": 25, "city": "Sofia"}
# print(data1["name"])
# data2 = {(5,6):"Rakia-10", "age": 8}
# print(data2[(5,6)])
# print(data2["age"])

# data2 = dict(name = "Rakia", age = 21, city = "Burgas")
# print(data2["name"])

# for i in data2:
#     print(i, '-',data2[i])

# data2.popitem()
# print(data2)
# print('keys : ', data2.keys())
# print('Values : ',data2.values())
# print('Items : ',data2.items())
# data2["price"] = 10
# print(data2)

# #  #11 – Множества (set и frozenset)
# data = set('hello')
# print(data)
# data.add('world')
# print(data)
# data.remove('o')
# print(data)
# print ('h' in data)
# print('--------------------')
# data = {1, 2, 3, 4, 5, 1.5, 2}
# print(data)
# data.add(6)
# print(data)
# data.update([7, 8, 9, True, "Rakia"])
# print(data)
# data.add(True)
# print(data)
# data1 = {1,2,True,1.5,"Rakia"}
# print(data1)
# data1.remove(1)
# print(data1)
# data1.pop()
# print(data1)
# data1.clear()
# print(data1)

# new_data = frozenset([1, 2, 3, 4, 5])
# print(new_data)

##12 – Функции (def, lambda)

# def test():
#     print("Hello from function")
# test()

# def test_function(word):
#     print("Hello ", word)
# test_function("Rakia")
# test_function(555)

# def summa(a, b):
#     res = a + b
#     print("Summa = ", res)
#     return res

# summa(5, 10)
# summa(1.5, 2.5)
# summa("Hello ", "Rakia")
# summa("Number ", str(5 ))

# def minimal(l):
#     minn = l[0]
#     for i in l:
#         if i < minn:
#             minn = i
#     return minn

# nums = [1, 2, 3, 4, 5, 22, 0.5,0.001, -1]
# result = minimal(nums)
# print("Min = ", result)

# func = lambda x,y: x * y
# print(func(5, 10))

## 13 – Работа с файлами за счет Питон

# file = open("data/test.txt", "w")
# file.write("Hello from Python file")
# file.write("\nThis is second line")
# file.write("\nThis is third line")
# file.close()

# data = input("Enter something: ")
# file = open("data/test.txt", "a")
# file.write(data + "\n")
# file.close()

# data = open("data/test.txt", "r")
# print(data.read())
# print('-----------------------')
# for line in data:
#     print(line, end="")
# data.close()

##14 – Обработчик исключений. Конструкция «try - except»
# x = 0
# while x == 0:
#     try:
#         x = int(input("Enter number: "))
#         x+= 5
#         print(x)
#         x = 1
#     except ValueError:
#         print("You should enter a number")

# try:
#     x = 5/1
#     y = int(input("Enter number: "))
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except ValueError:
#     print("You should enter a number")
# else:
#     print("This block will be executed if there is no exception")
# finally:
#     print("This block will be executed anyway")

#  #15 – Менеджер «With ... as» для работы с файлами
# try:
#     with open("data/test.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print("An error occurred:", e)
# else:
#     print("File was read successfully")
# finally:
#     print("This block will be executed anyway")
#     # file.close() - cannot be used here because the file is automatically closed after the with block

# try:
#     with open("data/test.txt", "r", encoding="utf-8") as file:   # open file and close it automatically after the block
#         print(file.read())
# except Exception as e:
#     print("An error occurred:", e)

##16 – Модули в языке Питон. Создание и работа с модулями
# import time
# time.sleep(3)
# print("Hello from module time")

# import datetime as dt
# import sys,os

# now = dt.datetime.now()
# print("Current date and time: ", now)
# print("Python version: ", sys.version)
# print("Current working directory: ", os.getcwd())
# print(sys.path)
# print(os.name)

# from math import sqrt as s, pi
# print("Square root of 16 is ", s(16))    
# print("Value of pi is ", pi)

# import mymodule
# mymodule.hello()
# result = mymodule.add_three_numbers(1, 2, 3)    
# print("Result of adding three numbers: ", result)

##17 – Основы ООП. Создание класса и объекта
# class Cat :
#     name = None
#     age = None
#     isHappy = None
#     def __init__(self, name, age, isHappy):  
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#     def get_data(self):
#         print("Name: ", self.name)
#         print("Age: ", self.age)
#         print("Is happy: ", self.isHappy)
    
#Конструкторът __init__
#Стартира автоматично при създаване на обекта:
#Методът set_data
#Той не се извиква автоматично.
#Трябва ръчно да го извикаш:    

# cat1 = Cat()
# cat1.name = "Murka" 
# cat1.age = 3
# cat1.isHappy = True

# cat2 = Cat()
# cat2.name = "Vaska"
# cat2.age = 5
# cat2.isHappy = False

# print("Cat1 name: ", cat1.name)
# print("Cat2 name: ", cat2.name)

# cat3 = Cat("Tom", 2, True)
# print("Cat3 name: ", cat3.name)
# cat3.get_data()



