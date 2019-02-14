from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin
from flaskblog import ma


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=False, nullable=True)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=True)
    posts = db.relationship('Post', backref='author', lazy=True)
    #def __repr__(self):
    #   return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'password')

class Category(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False,primary_key=True)
    num_acts = db.Column(db.Integer, nullable=True)
    posts = db.relationship('Post', backref='cat', lazy=True)
    def __init__(self, name):
        self.name = name

class CategorySchema(ma.Schema):
    class Meta:
        fields = ('name',)

    #def __repr__(self):
    #   return f"Category('{self.name}', '{self.num_acts}')"



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=True)
    date_posted = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    cat_name = db.Column(db.Integer, db.ForeignKey('category.name'), nullable=True)
    image_file = db.Column(db.String(20), nullable=True, default='default.jpg')
    upvotes = db.Column(db.Integer,nullable=True)
    def __init__(self,id,content,userid, cat_name):
        self.id = id
        #self.date_posted = date_posted
        self.content = content
        self.userid = userid
        self.cat_name = cat_name

    def __repr__(self):
        return f"Post('{self.id}' ,'{self.content}','{self.userid}','{self.cat_name}')"
    
class PostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'content', 'userid', 'cat_name')
