import sqlite3

# create a connection to access database
conn = sqlite3.connect('mytodos.db')
# declare a cursor
c = conn.cursor()
# command to select todos that are to be displayed
c.execute("SELECT rowid,todo FROM todos")
# fetchall() fetches all the rows from the last executed statement
todos = c.fetchall()
print(todos)
# executing and saving changes
conn.commit()
# closing the connection
conn.close()