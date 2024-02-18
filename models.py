# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

    def __init__(self, text):
        self.text = text

    def to_dict(self):
        return {
            'post_id': self.id,
            'text': self.text,
        }

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __init__(self, text, post_id):
        self.text = text
        self.post_id = post_id

    def to_dict(self):
        return {
            "comment_id": self.id,
            "comments": self.text,
            "post_id": self.post_id,
            "text": self.post.text  # Get the text of the associated post
        }
