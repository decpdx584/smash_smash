from flask import jsonify, redirect
from models import db, Fighter_one, Fighter_two

# # GET all
# def get_all_fighters():
#     all_fighters = Fighter.query.all()
#     results = [fighter.as_dict() for fighter in all_fighters]
#     return jsonify(results)

# # GET one
# def get_fighter(id):
#     fighter = Fighter.query.get(id)
#     if fighter:
#         return jsonify(fighter.as_dict())
#     else:
#         raise Exception('Sorry, could not find fighter at {}🤷‍♂️'.format(id))

# POST
def create_fighter(**form_kwargs):
    new_fighter1 = Fighter_one(**form_kwargs)
    new_fighter2 = Fighter_two(**form_kwargs)
    db.session.add(new_fighter1)
    db.session.add(new_fighter2)
    db.session.commit()
    print(f'{new_fighter1} successfully created!🎉', jsonify(new_fighter1.as_dict()))
    print(f'{new_fighter2} successfully created!🎉', jsonify(new_fighter2.as_dict()))

# PUT
# def update_fighter(id, **update_values):
#     fighter = Fighter.query.get(id)
#     if fighter:
#         for key, value in update_values.items():
#             setattr(fighter, key, value)
#         db.session.commit()
#         print('Successfully updated 🤘', jsonify(fighter.as_dict()))
#     else:
#         raise Exception('Sorry bud, no fighter at id {}'.format(id))

# # DELETE
# def destroy_fighter(id):
#     fighter = Fighter.query.get(id)
#     if fighter:
#         db.sessoion.delete(fighter)
#         db.session.commit()
#         print(f'Deuces, {fighter}!☮️')
#         return redirect('/fighters')
#     else:
#         raise Exception('Sorry bud, no fighter at id {}'.format(id))