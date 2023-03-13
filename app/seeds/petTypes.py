from app.models import db, User, PetType, environment, SCHEMA
from sqlalchemy.sql import text

def setGrowth(pet):
    if pet == 'Caterflitter':
        return 100

def seed_petTypes():
    caterflitter_r = PetType(
        pet = 'Caterflitter', 
        color = 'red', 
        maxGrowth = 100,
        mainImg = '',
        sadImg = '',
        madImg = ''
    )
    
    caterflitter_b = PetType(
        pet = 'Caterflitter', 
        color = 'blue', 
        maxGrowth = 100,
        mainImg = '',
        sadImg = '',
        madImg = ''
    )
    
    caterflitter_g = PetType(
        pet = 'Caterflitter', 
        color = 'green', 
        maxGrowth = 100,
        mainImg = '',
        sadImg = '',
        madImg = ''
    )
    
    caterflitter_y = PetType(
        pet = 'Caterflitter', 
        color = 'yellow', 
        maxGrowth = 100,
        mainImg = '',
        sadImg = '',
        madImg = ''
    )
    
    db.session.add(caterflitter_r)
    db.session.add(caterflitter_b)
    db.session.add(caterflitter_g)
    db.session.add(caterflitter_y)
    db.session.commit()
    
def undo_petTypes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.petTypes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM petTypes"))
        
    db.session.commit()