file_path = "C:\\Users\\admin\\desktop\\notes.txt"

file = open(file_path)
print(file.read())
file.close()

##### R-String 
file_path = r"C:\Users\admin\desktop\notes.txt" # RAW string, no escape simbols

file = open(file_path)
print(file.read())
file.close()
