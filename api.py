from models import app, Fighter
from flask import jsonify, request
from crud.fighter_crud import get_all_fighters, get_fighter

# ERROR HANDLER
@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception %s', (e))
    message_str = e.__str__()
    return jsonify(message=message_str.split(':')[0])

# ROUTES

## GET index
@app.route('/fighters')
def fighter_index_create():
    return get_all_fighters()

## GET show
@app.route('/fighters/<int:id>')
def fighter_show_put_delete(id):
    return get_fighter(id)

