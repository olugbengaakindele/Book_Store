from app import db,bcrypt
from datetime import datetime as dt
from app import login_manager
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(80), nullable = False)
    password = db.Column(db.String(100), nullable = False)
    date_of_reg = db.Column(db.DateTime, default = dt.utcnow())

    @classmethod
    def create_user(cls,user_name, user_email, user_password):
        user = cls(name = user_name, email= user_email.lower(), password = bcrypt.generate_password_hash(user_password).decode('utf-8'))
        
        db.session.add(user)
        db.session.commit()

        return user
    
@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


