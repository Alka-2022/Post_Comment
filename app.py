# app.py

from flask import Flask, send_file, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

# Define the database models
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

    def to_dict(self):
        return {
            'post_id': self.id,
            'text': self.text,
            'comments': [comment.to_dict() for comment in self.comments]
        }

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def to_dict(self):
        return {
            'comment_id': self.id,
            'text': self.text,
            'post_id': self.post_id
        }

# Define the route for the root URL
@app.route('/')
def home():
    return send_file('index.html')

# Create tables within the application context
def create_tables():
    with app.app_context():
        db.create_all()

# Call create_tables function before running the app
if __name__ == '__main__':
    create_tables()

# Endpoint to get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])

# Endpoint to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if 'text' not in data:
        abort(400, description="Missing text field")
    post = Post(text=data['text'])
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201

# Endpoint to add a comment to a post
@app.route('/posts/<int:post_id>/comments', methods=['POST'])
def add_comment(post_id):
    data = request.get_json()
    if 'text' not in data:
        abort(400, description="Missing text field")
    post = Post.query.get_or_404(post_id)
    comment = Comment(text=data['text'], post_id=post.id)
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
