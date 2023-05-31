from flaskblog.models import User, Post
from flask import Flask , render_template, url_for,flash,redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app

posts = [
    {
        'author':"Satwik",
        'title': 'Artificial intelligence in medieval times.',
        'content':'lorem ipsum dolor sit amet, consectetur adip',
        'date_posted':'Jan 7th 2023'
    },
    {
        'author':"Andrew Ng",
        'title': 'Artificial Intelligence is the new electricity.',
        'content':'lorem ipsum dolorsdsfsd df sit amet, consectetur adip',
        'date_posted':'Jan 11th 2020'
    }
]
@app.route("/")
@app.route("/home")
def home():
    '''Home page'''
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    '''about'''
    return render_template('about.html',title = 'About')

@app.route("/register", methods = ['GET','POST'])
def register():
    '''Registration'''
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for { form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title = 'Register',form = form)


@app.route("/login", methods = ['GET','POST'])
def login():
    '''Login'''
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in successfully!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsucessful, Please check username and password','danger')
            
    return render_template('login.html',title = 'Login',form = form)

