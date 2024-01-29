from app import app, db, Todo
from flask import request

#How I add stuff to the database
#variable = input()

#would have to turn this onto a variable probably an input variable
with app.app_context():
    db.create_all()

    db.session.add(Todo(todo_text=request.form['todo']))
    db.session.commit()

    all_todos = Todo.query.all()
    for todo in all_todos:
        print(todo.todo_text)



