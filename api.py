from models import app, Fighter
from flask import jsonify, request

@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception %s', (e))
    message_str = e.__str__()
    return jsonify(message=message_str.split(':')[0])