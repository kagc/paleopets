from app.models import db, User, PetType, Pet, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_pets():
    pet1 = Pet(
        ownerId = 2,
        petTypeId = 1,
        name = 'test_pet1',
        created_at = datetime(2023, 3, 13, 12, 00),
        # currGrowth = 0,
        hunger = 100,
        description = ''
    )
    
    db.session.add(pet1)
    db.session.commit()
    
def undo_pets():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.pets RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM pets"))
        
    db.session.commit()