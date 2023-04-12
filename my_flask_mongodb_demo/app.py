from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_todos
todos = db.todos


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        todo_name = request.form['input_Todo']
        todo_priority = request.form['input_Priority']
        todos.insert_one({'todo_name': todo_name, 'todo_priority': todo_priority})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)


# decorator which is a shortcut for @app.route("/<id>/delete/", method=["POST"])
@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


@app.post('/<id>/update/')
def update_priority(id):
    todos.update_one(filter={"_id": ObjectId(id)}, update={'$set': {"todo_priority": 'Low'}})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
