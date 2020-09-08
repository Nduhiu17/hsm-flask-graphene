from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(20), unique=True, nullable=False)
    password = db.Column(String(60), nullable=False)
    email = db.Column(String(100))
    stores = relationship('Store', backref='owner')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<User %r>' % self.id


class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(20), unique=True, nullable=False)
    user_id = db.Column(Integer, ForeignKey('users.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, soreid):
        return cls.query.filter_by(id=soreid).one()

    def __repr__(self):
        return '<Store %r>' % self.id
