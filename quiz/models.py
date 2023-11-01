from quiz import db, login_manager
from quiz import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), unique=True, nullable=False)
    email = db.Column(db.String(length=50), unique=True, nullable=False)
    password_hash = db.Column(db.String(length=60), nullable=False)
    points = db.Column(db.Integer(), default=0)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('UTF-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def zero_points(self):
        self.points = 0
        db.session.commit()

    def add_points(self):
        self.points += 10
        db.session.commit()


class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(length=500), unique=True, nullable=False)
    answer1 = db.Column(db.String(length=60), nullable=False)
    answer2 = db.Column(db.String(length=60), nullable=False)
    answer3 = db.Column(db.String(length=60), nullable=False)
    correct_answer = db.Column(db.String(length=60), nullable=False)




