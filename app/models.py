from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader

def user_load(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pitch = db.relationship('Mininfo', backref= 'author', lazy = 'dynamic')
    comments = db.relationship('Comments', backref='author', lazy= 'dynamic')

    @property
    def password(self):
        raise AttributeError("Permission denied")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'Author: {self.author}'

class Mininfo(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    pitch = db.Column(db.String(255))
    category = db.Column(db.String(255))
    date = db.Column(db.String(250), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comments', backref='title', lazy='dynamic')


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_info(cls, cate):
        pitch = Mininfo.query.filter_by(category=cate).all()
        return pitch
    def __repr__(self):
        return f"Mininfo ('{self.pitch}', '{self.date}')"


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(255))
    posted = db.Column(db.DateTime(250), default = datetime.utcnow)
    info_id = db.Column(db.Integer, db.ForeignKey('info.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_comments(cls, id):
        comments = Comments.query.filter_by(info_id=id ).all()
        return comments

    def __repr__(self):

        return f"Comments('{self.comment}', '{self.posted}')"






  


