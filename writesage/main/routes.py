from flask import Blueprint,render_template,request
from writesage.models import Post

main = Blueprint('main',__name__)


@main.route("/")
@main.route("/home")
def home():
    '''Home page'''
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page , per_page = 5)
    print(posts)
    return render_template('home.html', posts = posts)

@main.route("/about")
def about():
    '''about'''
    return render_template('about.html',title = 'About')
