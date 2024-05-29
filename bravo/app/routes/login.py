from flask import render_template, request
from . import routes_bp
from models.database import conn

@routes_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = conn.execute('SELECT * FROM users')
        for row in cursor:
            print(row)
        return f'Username: {username}, Password: {password}'
    return render_template('login.html')
