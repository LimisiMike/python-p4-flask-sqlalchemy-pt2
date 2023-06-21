#!/usr/bin/env python3

from random import choice as rc

from faker import Faker

from app import app
from models import db, Owner, Pet

db.init_app(app)

fake = Faker()

with app.app_context(): #Creates an application context
    # Delete all records from the database
    Pet.query.delete()
    Owner.query.delete()
    
    # Make a list of owner and pet instances
    owners = []
    for n in range(50):
        owner = Owner(name=fake.name())
        owner.append(owner)
        
    db.session.add_add(owners)
    
    pets = []
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    for n in range(100):
        pet = Pet(name=fake.first_name(), species=rc(species), owner=rc(owners))
        pets.append(pet)
    
    # commit the transaction
    db.session.add_all(pets)
    db.session.commit()


