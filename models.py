from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/smash_dev'
db = SQLAlchemy(app)

date_args = db.Table('date_args',
    db.Column('date_id', db.Integer, db.ForeignKey('date_id'), primary_key=True),
    db.Column('argument_id', db.Integer, db.ForeignKey('argument_id'), primary_key=True)
)

class Fighter(db.Model):
    __tablename__ = 'fighters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    universe = db.Column(db.String, nullable=False)
    availability = db.Column(db.String)
    final_smash = db.Column(db.String)
    quote = db.Column(db.String)
    wiki_url = db.Column(db.String)
    dates = db.relationship('Date', backref='fighter', lazy=True)

    def __repr__(self):
        return f'Fighter(id={self.id}, name="{self.name}", universe="{self.universe}", availability="{self.availability}", final_smash="{self.final_smash}", attributes="{self.attributes}", wiki_url="{self.wiki_url}")'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Date(db.Model):
    __tablename__ = 'dates'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    bio = db.Column(db.String(150))

    fighter_one = db.relationship('Fighter', backref='single', lazy=True)
    fighter_two = db.relationship('Fighter', backref='single', lazy=True)
    arguments = db.relationship('Argument', backref='date', lazy=True)

    def __repr__(self):
        return f'Date(id={self.id}, name="{self.name}", email="{self.email}")'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Argument(db.Model):
    __tablename__ = 'arguments'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50))
    body = db.Column(db.String, nullable=False)
    date_id = db.Column(db.Integer, db.ForeignKey('date_id'), nullable=False)