from .db import db, environment, SCHEMA, add_prefix_for_prod
from .user import User
from. petType import PetType
from datetime import datetime

class Pet(db.Model):
    __tablename__ = 'pets'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    ownerId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    petTypeId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("petTypes.id")), nullable=False)
    name = db.Column(db.String(40), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    currGrowth = db.Column(db.DECIMAL(50,2), nullable=False)
    hunger = db.Column(db.DECIMAL(50,2), nullable=False)
    description = db.Column(db.String(4000))
    # img = db.Column(db.String(1000), nullable=False)
    
    owner = db.relationship("User", back_populates="pets")
    petType = db.relationship("PetType", back_populates="pets")
    
    def to_dict_pet(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'hunger': self.hunger,
            'description': self.description,
            'owner': User.query.get(self.ownerId).to_dict(),
            'petDetails': PetType.query.get(self.petTypeId).to_dict_petType()
        }
        
        