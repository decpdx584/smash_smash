from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/smash_dev'
db = SQLAlchemy(app)

# fighter_dates = db.Table('fighter_dates',
#     db.Column('fighter_id', db.Integer, db.ForeignKey('fighters.id'), primary_key=True)
#     db.Column('date_id', db.Integer, db.ForeignKey('dates.id'), primary_key=True),
# )

with app.app_context():
    class Fighter_one(db.Model):
        __tablename__ = 'fighters_one'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, nullable=False)
        universe = db.Column(db.String, nullable=False)
        availability = db.Column(db.String)
        final_smash = db.Column(db.String)
        quote = db.Column(db.String)
        wiki_url = db.Column(db.String)

        dates = db.relationship('Date', backref='fighter_one', lazy=True)

        def __repr__(self):
            return f'Fighter(id={self.id}, name="{self.name}", universe="{self.universe}", availability="{self.availability}", final_smash="{self.final_smash}", quote="{self.quote}", wiki_url="{self.wiki_url}")'

        def as_dict(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    class Fighter_two(db.Model):
        __tablename__ = 'fighters_two'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, nullable=False)
        universe = db.Column(db.String, nullable=False)
        availability = db.Column(db.String)
        final_smash = db.Column(db.String)
        quote = db.Column(db.String)
        wiki_url = db.Column(db.String)

        dates = db.relationship('Date', backref='fighter_two', lazy=True)

        def __repr__(self):
            return f'Fighter(id={self.id}, name="{self.name}", universe="{self.universe}", availability="{self.availability}", final_smash="{self.final_smash}", quote="{self.quote}", wiki_url="{self.wiki_url}")'

        def as_dict(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    date_args = db.Table('date_args',
        db.Column('date_id', db.Integer, db.ForeignKey('dates.id'), primary_key=True),
        db.Column('argument_id', db.Integer, db.ForeignKey('arguments.id'), primary_key=True)
    )

    class Date(db.Model):
        __tablename__ = 'dates'

        id = db.Column(db.Integer, primary_key=True)
        fighter_one_id = db.Column(db.Integer, db.ForeignKey('fighters_one.id', ondelete='SET NULL'), nullable=False)
        fighter_two_id = db.Column(db.Integer, db.ForeignKey('fighters_two.id', ondelete='SET NULL'), nullable=False)

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
        date_id = db.Column(db.Integer, db.ForeignKey('dates.id', ondelete='SET NULL'), nullable=False)

        def __repr__(self):
            return f'Argument(id={self.id}, author="{self.author}", body="{self.body}")'

        def as_dict(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}