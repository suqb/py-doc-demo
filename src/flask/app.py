# pip install Flask
from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/user/<int:user_id>')
def user(user_id):
    return 'User %d' % user_id

@app.route('/user/list')
def user_list():
    page = request.args.get('page', 1, type=int)
    return 'User list page %d' % page


# python -m flask run
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)

