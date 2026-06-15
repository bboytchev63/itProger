name = input('Yor Name : ')
print('Hellow ', name)

num1 = input('N1 ')
num2 = input('N2 ')
print('Sum as str ', num1 + num2)
try:
    print("Sum as Numbers ", int(num1) + int(num2))
except:
    print("Sum as Numbers ", float(num1) + float(num2))
