from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/smash_dev'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    bio = db.Column(db.String(150))

    def __repr__(self):
        return f'User(id={self.id}, name="{self.name}", email="{self.email}")'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Fighter(db.Model):
    __tablename__ = 'fighters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    universe = db.Column(db.String, nullable=False)
    availability = db.Column(db.String)
    final_smash = db.Column(db.String)
    attributes = db.Column(db.String)

    def __repr__(self):
        return f'Fighter(id={self.id}, name="{self.name}", universe="{self.universe}", availability="{self.availability}", final_smash="{self.final_smash}", attributes="{self.attributes}")'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}