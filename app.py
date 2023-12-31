from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Your User and Task models go here (ensure they are defined properly)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Task('{self.content}')"

# Route to render the index.html template
@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)

# Ensure this block only runs when executed directly, not when imported as a module
if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True)


