from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos


# In this route, you pass the tuple ('GET', 'POST') to the methods parameter to allow both GET and POST requests.
# GET requests are used to retrieve data from the server. POST requests are used to post data to a specific route.
# By default, only GET requests are allowed.
# When the user first requests the / route using a GET request, a template file called index.html will be rendered.
@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)


# decorator which is a shortcut for @app.route("/<id>/delete/", method=["POST"])
@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
