from flask import Flask, request, Response

from datetime import datetime

from functools import wraps

from models import db, Feedback, UserProfile

from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

app.config.from_object('config')

db.init_app(app)


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    # db.session.UserProfile(UserProfile.user_pass).filter(UserProfile.user_name == username)
    try:
        p = db.session.query(UserProfile).filter(UserProfile.user_name == username).first().user_pass
    except:
        return False

    return password == p


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated


@app.route('/feedback', methods=['POST'])
def feedback():
    print (request.args)

    f = Feedback(product_id=request.args['product_id'],
                 name=request.args['name'],
				 email=request.args['email'],
                 rating=request.args['rating'],
                 comment=request.args['comment'])
    db.session.add(f)
    db.session.commit()

    return 'saved'


@app.route('/get_rating', methods=['POST'])
@requires_auth
def get_rating():
    from_dt = datetime.strptime(request.args['from_dt'], '%Y-%m-%d %H:%M:%S')
    to_dt = datetime.strptime(request.args['to_dt'], '%Y-%m-%d %H:%M:%S')

    cou = (db.session.query(Feedback).filter(Feedback.rating == request.args['rating'],
                                       Feedback.feedback_datetime >= from_dt,
                                       Feedback.feedback_datetime <= to_dt).count())

    print (cou)

    return str(cou)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
