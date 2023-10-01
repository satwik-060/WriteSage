from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField

class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    desc = TextAreaField('Description',validators = [DataRequired()])
    content = CKEditorField('Content',validators = [DataRequired()])
    submit = SubmitField('Post')
    
