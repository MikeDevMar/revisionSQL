from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#db =sqlite3.connect('books-collection.db')
#cursor = db.cursor()
#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
#db.commit()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique = True, nullable=False)
    author= db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

#db.create_all()
all_books = []

'''new_book = Book(
    title= 'mango shango',
    author='ahmed el awadi',
    rating=5
)
#db.session.add(new_book)
db.session.commit()'''

@app.route('/')
def home():
    return render_template('index.html', books=all_books)



@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book= {
            'title': request.form['title'],
            "author": request.form['author'],
            'rating':request.form['rating']
        }
        all_books.append(new_book)
        return redirect(url_for('home'))
    return render_template('add.html')




if __name__ == "__main__":
    app.run(debug=True)
