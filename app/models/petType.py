from .db import db, environment, SCHEMA, add_prefix_for_prod

class PetType(db.Model):
    __tablename__ = 'petTypes'
    
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
        
    id = db.Column(db.Integer, primary_key=True)
    pet = db.Column(db.String(40), nullable=False)
    color = db.Column(db.String(40), nullable=False)
    maxGrowth = db.Column(db.DECIMAL(50, 2), nullable=False)
    mainImg = db.Column(db.String(1000), nullable=False)
    sadImg = db.Column(db.String(1000), nullable=False)
    madImg = db.Column(db.String(1000), nullable=False)
    
    pets = db.relationship("Pet", back_populates="petType", cascade="all, delete")
    
    def to_dict_petType(self):
        'id': self.id
        'pet': self.pet
        'color': self.color
        'maxGrowth': self.maxGrowth
        'mainImg': self.mainImg
        'sadImg': self.sadImg
        'madImg': self.madImg