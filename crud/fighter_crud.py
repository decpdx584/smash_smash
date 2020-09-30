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

# POST
def create_fighter(**form_kwargs):
    new_fighter = Fighter(**form_kwargs)
    db.session.add(new_fighter)
    db.session.commit()
    return jsonify(new_fighter.as_dict())

# PUT
def update_fighter(id, **update_values):
    fighter = Fighter.query.get(id)
    if fighter:
        for key, value in update_values.items():
            setattr(fighter, key, value)
        db.session.commit()
        return jsonify(fighter.as_dict())
    else:
        raise Exception('Sorry bud, no fighter at id {}'.format(id))

# DELETE
def destroy_fighter(id):
    fighter = Fighter.query.get(id)
    if fighter:
        db.sessoion.delete(fighter)
        db.session.commit()
        return redirect('/fighters')
    else:
        raise Exception('Sorry bud, no fighter at id {}'.format(id))