# https://www.youtube.com/watch?v=LffQVBq3P9o
# Python Context Managers - Visually Explained

# with open("whisky.txt" ,"w") as file:
#     file.write('Single malt whisky\n')
#     file.write('Blended malt whisky\n')
#     file.write("Single cask\n") 


# with open("whisky.txt","r") as input_file, open("SortedWhisky.txt", "w") as output_file:
#     titles = input_file.read().split("\n")
#     titles.sort()
#     output_file.write("\n".join(titles))
# print(titles)

##################################
import sqlite3
titles = [
    (1,"Lagavulin"),
    (2,"Glenfiddich"),
    (3,"Ardbeg"),
    (4,"Macallan"),
    (5,"Talisker"),
    (6,"Highland Park")
]

with sqlite3.connect("DATA/whisky.db") as connection:
    cursor = connection.cursor()
    # execute SQL 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS WHISKY(
                   id INTEGER,
                   name_whisky TEXT)

    ''')
    for id, name_whisky in titles:
        cursor.execute("INSERT INTO whisky VALUES (?,?)" , (id, name_whisky))
    


