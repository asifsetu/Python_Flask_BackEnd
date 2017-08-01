
from models import db, Product, UserProfile
from flask import Flask

app = Flask(__name__)

app.config.from_object('config')

db.init_app(app)

with app.app_context():
    # Extensions like Flask-SQLAlchemy now know what the "current" app
    # is while within this block. Therefore, you can now run........
    db.create_all()

    # add products to DB

    prod1 = Product(product_id='0815', product_name='Foobar-Soundsystem')
    db.session.add(prod1)

    prod2 = Product(product_id='1337', product_name='Soundblaster Pro')
    db.session.add(prod2)

    # add admin user to DB

    admin = UserProfile(user_id='1', user_name='admin', user_email='admin@admin.com', user_pass='secret!')
    db.session.add(admin)

    db.session.commit()