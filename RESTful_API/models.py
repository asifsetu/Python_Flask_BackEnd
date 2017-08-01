from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

import datetime


#create datatype aliases
Column = db.Column
String = db.String
Unicode = db.Unicode
Model = db.Model
Integer = db.Integer
ForeignKey = db.ForeignKey
Date = db.Date
DateTime = db.DateTime
Boolean = db.Boolean


class UserProfile(Model):
    __tablename__ = 'userprofile'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(45),unique=True)
    user_email = Column(String(45),unique=True)
    user_pass = Column(String(45))


class Product(Model):
    __tablename__ = 'product'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(45))


class Feedback(Model):
    __tablename__ = 'feedback'
    feedback_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.product_id'))
    name = Column(String(45),nullable=True)
    email = Column(String(45),nullable=True)
    rating = Column(Integer)
    comment = Column(String(250),nullable=True)
    feedback_datetime = Column(DateTime, default=datetime.datetime.utcnow)




