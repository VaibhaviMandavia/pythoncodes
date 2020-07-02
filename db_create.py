import sqlite3

# create a database
# create a connection to access database
conn = sqlite3.connect('mytodos.db')
# declare cursor
# cursor holds the rows returned by a SQL statement
c = conn.cursor()
# command to create a table
c.execute('''CREATE TABLE todos (todo text)''')
# executing and saving changes
conn.commit()
# closing the connection
conn.close()