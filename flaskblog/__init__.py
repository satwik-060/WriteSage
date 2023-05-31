from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '1f114f296041cf407f10120252bad889'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes