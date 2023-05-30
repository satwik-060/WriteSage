'''Learning Flask'''
from flask import Flask , render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '1f114f296041cf407f10120252bad889'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow())
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"
    

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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8002, debug=True)
 