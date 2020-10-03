from models import app, Fighter_one, Fighter_two
from flask import Flask, jsonify, request, g, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from crud.fighter_crud import get_all_fighters, get_fighter, create_fighter, update_fighter, destroy_fighter



# ERROR HANDLER
@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception %s', (e))
    message_str = e.__str__()
    return jsonify(message=message_str.split(':')[0])

# VIEWS
@app.route('/')
def home():
    return render_template('home.html')

# ROUTES

## GET index, POST new
@app.route('/fighters', methods=['GET', 'POST'])
def fighter_index_create():
    if request.method == 'GET':
        return get_all_fighters()
    if request.method == 'POST':
        return create_fighter(**request.form)

## GET show, PUT update, DELETE destroy
@app.route('/fighters/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def fighter_show_put_delete(id):
    if request.method == 'GET':
        return get_user(id)
    if request.method == 'PUT':
        return update_user(id, **request.form)
    if request.method == 'DELETE':
        return destroy_user(id)


