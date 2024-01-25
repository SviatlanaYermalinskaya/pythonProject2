import sqlite3

con = sqlite3.connect('base3.db')
cursor = con.cursor()

cursor.execute("""create table if not exists people(years integer, name text, surname text);""")

for i in range(3):
    y = int(input("Please, enter age: "))
    n = input("Please, enter name: ")
    s = input("Please, enter surname: ")
    cursor.execute("""insert into  people values (?, ?, ?);""", (y, n, s))

con.commit()
con.close()


