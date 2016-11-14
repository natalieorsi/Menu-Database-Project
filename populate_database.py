from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, Menu Item

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine
#Create session, required to execute database operations in SQLAlchemy
DBSession = sessionmaker(bind = engine)
session = DBSession()

pizza = Restaurant(name = "Yeasty Pomodoro")
session.add(pizza)
session.commit() #added to Restaurant table

#show me all the restaurants - will return objects
session.query(Restaurant).all()

whitepie = MenuItem(name = "White Pizza", description = "Hold the sauce!", course = "Entree", price = "$12.00", restaurant = "Yeasty Pomodoro")
session.commit() #added to Menu table, linked to Restaurant via foreign key

#show me all the foods - returns objects
session.query(MenuItem).all()

