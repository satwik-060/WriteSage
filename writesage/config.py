import os  

class Config:
    SECRET_KEY = '1f114f296041cf407f10120252bad889'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'perisetla.satwik176@gmail.com'
    MAIL_PASSWORD = os.environ.get('DB_PASSWORD')
    CKEDITOR_PKG_TYPE = 'full-all'