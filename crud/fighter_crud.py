from flask import Flask, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, app, Fighter_one, Fighter_two

# GET all
def get_all_fighters():
    all_fighters = Fighter_one.query.all()
    # results = [all_fighters.as_dict() for fighter in all_fighters]
    # return jsonify(all_fighters)
    return all_fighters

# GET one
def get_fighter(id):
    fighter = Fighter_one.query.get(id)
    if fighter:
        return jsonify(fighter.as_dict())
    else:
        raise Exception('Sorry, could not find fighter at {}🤷‍♂️'.format(id))

# POST
def create_fighter(**form_kwargs):
    new_fighter1 = Fighter_one(**form_kwargs)
    new_fighter2 = Fighter_two(**form_kwargs)
    db.session.add(new_fighter1)
    db.session.add(new_fighter2)
    db.session.commit()
    print(f'{new_fighter1} successfully created!🎉')

# PUT
def update_fighter(id, **update_values):
    fighter1 = Fighter_one.query.get(id)
    if fighter1:
        for key, value in update_values.items():
            setattr(fighter1, key, value)
        db.session.commit()
        print('Successfully updated 🤘', jsonify(fighter1.as_dict()))
    else:
        raise Exception('Sorry bud, no fighter at id {}'.format(id))

    fighter2 = Fighter_two.query.get(id)
    if fighter2:
        for key, value in update_values.items():
            setattr(fighter2, key, value)
        db.session.commit()
        print('Successfully updated 🤘', jsonify(fighter2.as_dict()))
    else:
        raise Exception('Sorry bud, no fighter at id {}'.format(id))

# DELETE
def destroy_fighter(id):
    fighter1 = Fighter_one.query.get(id)
    fighter2 = Fighter_two.query.get(id)
    if fighter1:
        db.sessoion.delete(fighter1)
        db.session.commit()
        print(f'Deuces, {fighter1}!☮️')
        return redirect('/fighters_one')
    else:
        raise Exception('Sorry bud, no fighter at id {}'.format(id))
    
    if fighter2:
        db.sessoion.delete(fighter)
        db.session.commit()
        print(f'Deuces, {fighter}!☮️')
        return redirect('/fighters_one')
    else:
        raise Exception('Sorry bud, no fighter at id {}'.format(id))