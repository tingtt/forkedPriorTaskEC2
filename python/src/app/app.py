from flask import Flask, url_for, redirect, render_template

from DataStore.MySQL import MySQL

dns = {
    'user': 'root',
    'host': 'mysql',
    'password': 'root',
    'database': 'sample_db'
}
mysql = MySQL(**dns)

app = Flask(__name__)


@app.route('/')
def main():
    props = {
        'title': 'Step-by-Step Flask - index',
        'msg': 'Welcome to Index Page.'
    }
    html = render_template('index.html', props=props)
    return html


@app.route('/hello')
def hello():
    props = {'title': 'Step-by-Step Flask - hello', 'msg': 'Hello World.'}
    html = render_template('hello.html', props=props)
    return html


@app.route('/users')
def users():
    props = {'title': 'Users List', 'msg': 'Users List'}
    stmt = 'SELECT * FROM users'
    users = mysql.query(stmt)
    html = render_template('users.html', props=props, users=users)
    return html


@app.route('/users/<int:id>')
def user(id):
    props = {'title': 'User Information', 'msg': 'User Information'}
    stmt = 'SELECT * FROM users WHERE id = ?'
    user = mysql.query(stmt, id, prepared=True)
    html = render_template('user.html', props=props, user=user[0])
    return html


@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)
