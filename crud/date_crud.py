from flask import jsonify, redirect
from models import db, Date

# GET all
def get_all_dates():
    all_dates = Date.query.all()
    results = [date.as_dict() for date in all_dates]
    return jsonify(results)

# GET one
def get_date(id):
    date = Date.query.get(id)
    if date:
        return jsonify(date.as_dict())
    else:
        raise Exception('Sorry, could not find date at {}🤷‍♂️'.format(id))

# POST

# DELETE