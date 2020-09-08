# import graphene
# from sqlalchemy import *
# from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
#
# from app import db
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     username = Column(String(20),unique=True,nullable=False)
#     password = Column(String(60),nullable=False)
#     email = Column(String(100))
#     stores = relationship('Store',backref='owner')
#
#     def __repr__(self):
#         return '<User %r>' % self.email
#
#
# class Store(db.Model):
#     __tablename__ = 'stores'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(20),unique=True,nullable=False)
#     user_id = Column(Integer,ForeignKey('users.id'))
#
#     def __repr__(self):
#         return '<Store %r>' % self.name
#
