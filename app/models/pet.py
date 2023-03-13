from .db import db, environment, SCHEMA, add_prefix_for_prod
from .user import User
from datetime import datetime

class Pet(db.Model):
    __tablename__ = 'pets'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    name = db.Column(db.String(40), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    
    owner = db.relationship("User", back_populates="pets")