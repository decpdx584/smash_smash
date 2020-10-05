from flask import jsonify, redirect
from models import db, Date

# GET all
def get_all_dates():
    all_dates = Date.query.all()
    # results = [date.as_dict() for date in all_dates]
    return all_dates

# GET one
def get_date(id):
    date = Date.query.get(id)
    if date:
        return date
    else:
        raise Exception('Sorry, could not find date at {}🤷‍♂️'.format(id))

# POST
def create_date(**form_kwargs):
    new_date = Date(**form_kwargs)
    db.session.add(new_date)
    db.session.commit()
    print(f'{new_date} successfully created!🌈')

# DELETE