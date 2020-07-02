import sqlite3

# collecting todo
todo = input("enter your todo: ")
# create a connection to access database
conn = sqlite3.connect('mytodos.db')
# declare cursor
c = conn.cursor()
# command to insert/add todos
c.execute("INSERT INTO todos VALUES ('"+todo+"')")
print(todo, "is inserted")
# executing and saving changes
conn.commit()
# closing the connection
conn.close()
