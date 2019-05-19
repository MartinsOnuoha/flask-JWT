# project/server/models.py
from datetime import datetime
from project.server import app, db, bcrypt

class User(db.Model):
  """User model for storing user related data"""
  __tablename__ = "users"

  # setup each user column fields ( id, email, password, registered_on, is_admin)
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  email = db.Column(db.String(255), unique=True, nullable=False)
  password = db.Column(db.String(255), nullable=False)
  registered_on = db.Column(db.DateTime, nullable=False)
  is_admin = db.Column(db.Boolean, nullable=False, default=False)

  # constructor
  def __init__(self, email, password, is_admin=False):
    self.email = email
    self.password = bcrypt.generate_password_hash(password, app.config.get('BCRYPT_LOG_ROUNDS')).decode()
    self.registered_on = datetime.now()
    self.is_admin = is_admin

  # Encode authentication token
  def encode_auth_token(self, user_id):
    """
      Generates the Auth Token
      :returns: string 
    """
    
