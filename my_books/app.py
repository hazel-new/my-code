from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_books
books = db.books


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        book_name = request.form['input_BookName']
        book_type = request.form['input_BookType']
        books.insert_one({'book_name': book_name, 'book_type': book_type})
        return redirect(url_for('index'))

    all_books = books.find()
    return render_template('index.html', books=all_books)


# decorator which is a shortcut for @app.route("/<id>/delete/", method=["POST"])
@app.post('/<id>/delete/')
def delete(id):
    books.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))


@app.post('/<id>/update/')
def update_type(id):
    books.update_one(filter={"_id": ObjectId(id)}, update={'$set': {"book_type": '文学'}})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
