from flask import jsonify, redirect
from models import db, Fighter

# GET all
def get_all_fighters():
    all_fighters = Fighter.query.all()
    results = [fighter.as_dict() for fighter in all_fighters]
    return jsonify(results)

# GET one
def get_fighter(id):
    fighter = Fighter.query.get(id)
    if fighter:
        return jsonify(fighter.as_dict())
    else:
        raise Exception('Sorry, could not find fighter at {}🤷‍♂️'.format(id))