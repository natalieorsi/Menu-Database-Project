#######Configuration##########
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

##Class##
#representation of table as a python class
#extends the Base class
#nested inside will be table and mapper code
#camel-cased
class Restaurant(Base):
	##Table##
	#syntax: __tablename__ = 'table_name'
	__tablename__ = 'restaurant'
	##Mapper##
	name = Column(String(80), nullable = False) #String type w max length 80, never Null
	id = Column(Integer, primary_key = True) #another Column, this time int 

class Menu(Base):
	##Table##
	__tablename__ = 'menu_item'
	##Mapper##
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)

	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(Integer, ForeignKey('restaurant.id')) #link it to the Restaurant Table's foreign ID key
	restaurant = relationship(Restaurant)
		


#######end of file Configuration#########
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)