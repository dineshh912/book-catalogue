from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login.utils import login_required
from app import app
from app.forms import LoginForm, RegistrationForm, SearchForm
from flask_login import current_user, login_user, logout_user
from app.models import User, Books, BookSchema
from app import db
import requests



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@login_required
def index():
    form = SearchForm()
    books = Books.query.order_by(Books.timestamp.desc()).all()
    
    if form.validate_on_submit():
        if(form.type.data == "isbn"):
            url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{form.search.data}"
        else:
            url = f"https://www.googleapis.com/books/v1/volumes?q=title:{form.search.data}"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        book_list_json = response.json()
        if(book_list_json["totalItems"] != 0):
            book_list = book_list_json["items"]
        else:
            book_list = "No result found"
        return render_template("index.html", form=form, books = books, book_list=book_list)
    return render_template("index.html", form=form, books = books, book_list=[])


@app.route("/add", methods=["GET","POST"])
def addBooks():
    data = request.get_json()
    books = Books(user_id=current_user.get_id(),
                 book_id=data["book_id"],
                 book_title=data["info"]["title"],
                 book_thumb=data["info"]["img_url"],
                 book_author=data["info"]["author"],
                 book_page=data["info"]["pagecount"],
                 book_rating=data["info"]["averageRating"])
    db.session.add(books)
    db.session.commit()  
    return "added"


@app.route("/delete/<id>")
def deleteBooks(id):
    book = Books.query.filter_by(user_id=current_user.get_id(), book_id=id).first()
    db.session.delete(book)
    db.session.commit()
    
    flash("Deleted")

    return redirect(url_for('index'))


