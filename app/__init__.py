from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '3e768f29134da9c4067b8095f7c8ab68f31d871316f6b53f001d07317831353d5d1a3a48138d4b35424958c484ae3e1348a806d0063b464e946531e1227ffc87'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category="info"

from app import routes