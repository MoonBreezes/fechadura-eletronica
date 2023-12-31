from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from app.database import db
from flask_login import UserMixin
from datetime import datetime
import bcrypt
# used for user model, maybe its good to have for all models

''' Represents admin, lock_users and locks
    Used for locks to have the same underlying security as regular users
'''
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    __tablename__ = 'user'
    # username can be 0 (admin), room number(4 digits), 
    # or enrollment id(10 digits)
    username = db.Column('username', db.String(32), unique=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(64)) 
    created = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String, default="lock_user") # can be admin, lock, lock_user
    authenticated = db.Column(db.Boolean, default=False)
    
    # properties implemented in UserMixin
    def is_active(self):
        return True

    def get_username(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
    
    def what_role(self):
        return self.role
    
    ''' Row like object: 
        dict with key:value representing col_name:row_value
    '''
    @property
    def as_row(self):
        return self.__dict__

''' Permissions table, can ingress in a room?
'''
class Permissions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    __tablename__ = 'permissions'
    room = ForeignKey('user.username')
    user = ForeignKey('user.username')
    created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def get_username(self):
        return self.user
    
    def get_room(self):
        return self.room

    ''' Row like object: 
        dict with key:value representing col_name:row_value
    '''
    @property
    def as_row(self):
        return self.__dict__

''' List of users that used the locks
'''
class Entry_List(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    __tablename__ = 'entry_list'
    room = db.Column(db.String(64)) 
    author = db.Column(db.String(64)) 
    date = db.Column(db.DateTime, default=datetime.utcnow)
    success = db.Column(db.Boolean, default=False)
    
    def is_active(self):
        return True

    def get_username(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
    
    ''' Row like object: 
        dict with key:value representing col_name:row_value
    '''
    @property
    def as_row(self):
        return self.__dict__

