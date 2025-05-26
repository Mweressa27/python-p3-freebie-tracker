#!/usr/bin/env python3

# Script goes here!
from models import Dev, Company, Freebie, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create companies and devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
company1 = Company(name="Flatiron", founding_year=2012)
company2 = Company(name="Replit", founding_year=2017)

# Add them 
session.add_all([dev1, dev2, company1, company2])
session.commit()

# Give out freebies
freebie1 = Freebie(item_name="Notebook", value=1, dev=dev1, company=company1)
freebie2 = Freebie(item_name="T-shirt", value=10, dev=dev2, company=company1)
freebie3 = Freebie(item_name="Water Bottle", value=5, dev=dev1, company=company2)

session.add_all([freebie1, freebie2, freebie3])
session.commit()
