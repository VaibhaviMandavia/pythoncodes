# creating a todo application in Flask

from flask import Flask
from flask_cors import CORS
import sqlite3
import json

# instantiating a Flask object by passing __name__ argument to the Flask constructor
# the Flask constructor has one required argument which is the name of the application package
app = Flask(__name__)
CORS(app)


# CREATING ROUTES
# when the application receives a request where the path is "/", the hello() function will be invoked to complete the request
@app.route('/')
def hello():
    return "hello from server"


# ADDING TODOS
# when the application receives a request where the path is "/addtodos/<todo>", the addtodos() function will be invoked to complete the request
@app.route('/addtodos/<todo>')
def addtodo(todo):
    # creating a connection to the database
    conn = sqlite3.connect('mytodos.db')
    c = conn.cursor()
    # insert todos into the table
    c.execute("INSERT INTO todos VALUES ('"+todo+"')")
    # saving changes
    conn.commit() 
    # closing the connection
    conn.close()
    return "todo inserted"


# GETTING TODOS
# when the application receives a request where the path is "/gettodos/", the gettodos() function will be invoked to complete the request
@app.route('/gettodos/')
def gettodos():
    # creating a connection to the database
    conn = sqlite3.connect('mytodos.db')
    c = conn.cursor()
    # select the columns that are should be displayed
    c.execute("SELECT rowid,todo FROM todos")
    # fetchall() fetches all the rows from the last executed statement
    todos = c.fetchall()
    todo_array = []
    for t in todos:
        todo_array.append(t)
    return json.dumps(todo_array)


# DELETING TODOS
# when the application receives a request where the path is "/deletetodos/<rid>", the deletetodos() function will be invoked to complete the request
@app.route('/deletetodos/<rid>')
def deletetodos(rid):
    # creating a connection to the database
    conn = sqlite3.connect('mytodos.db')
    c = conn.cursor()
    # delete a particular value by filtering the selection
    c.execute("DELETE FROM todos WHERE rowid="+rid)
    # saving changes
    conn.commit()
    # closing the connection
    conn.close()
    return "todo deleted"
    

# UPDATING TODOS
# when the application receives a request where the path is "/updatetodos/<rid>/<new_value>", the updatetodos() function will be invoked to complete the request
@app.route('/updatetodos/<rid>/<new_value>')
def updatetodos(rid,new_value):
    # creating a connection to the database
    conn = sqlite3.connect('mytodos.db')
    c = conn.cursor()
    c.execute("UPDATE todos SET todo='"+ new_value +"' WHERE rowid='"+rid+"'")
    # saving changes
    conn.commit()
    # closing the connection
    conn.close()
    return "todo updated"

app.run(port="5000")