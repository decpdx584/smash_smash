from models import db, app, Fighter_one, Fighter_two, Date, Argument
from flask import Flask, jsonify, request, g, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from crud.fighter_crud import get_all_fighters, get_fighter, create_fighter, update_fighter, destroy_fighter
from crud.date_crud import get_all_dates, get_date

# ERROR HANDLER
@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception %s', (e))
    message_str = e.__str__()
    return jsonify(message=message_str.split(':')[0])


# ROUTES

@app.route('/')
def home():
    return render_template('home.html')

## Fighters:
### GET index, POST new
@app.route('/singles', methods=['GET', 'POST'])
def fighter_index_create():
    if request.method == 'GET':
        return render_template('singles/singles.html', singles = get_all_fighters())
    if request.method == 'POST':
        return create_fighter(**request.form)

## GET show, PUT update, DELETE destroy
@app.route('/singles/<int:id>')
def fighter_show_put_delete(id):
    if request.method == 'GET':
        return render_template('singles/single_show.html', single = get_fighter(id))
    if request.method == 'PUT':
        return update_user(id, **request.form)
    if request.method == 'DELETE':
        return destroy_user(id)

## Dates:
### GET index, POST new
@app.route('/dates', methods=['GET', 'POST'])
def date_index_create():
    if request.method == 'GET':
        return render_template('dates/dates.html', dates = get_all_dates())
    if request.method == 'POST':
        return create_fighter(**request.form)

## GET show, PUT update, DELETE destroy
@app.route('/dates/<int:id>')
def date_show_put_delete(id):
    if request.method == 'GET':
        return render_template('dates/date_show.html', date = get_date(id))
    if request.method == 'PUT':
        return update_user(id, **request.form)
    if request.method == 'DELETE':
        return destroy_user(id)
