from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup3 import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu3.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants/')
def restaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('index.html', restaurants=restaurants)


@app.route('/restaurants/newRestaurant/')
def newRestaurant():
    return 'new restaurant'


@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    return 'Menu do restaurant'


@app.route('/restaurants/<int:restaurant_id>/editRestaurant/')
def editRestaurant(restaurant_id):
    return 'edit restaurant'


@app.route('/restaurants/<int:restaurant_id>/deleteRestaurant/')
def deleteRestaurant(restaurant_id):
    return 'delet restaurant'


@app.route('/restaurants/<int:restaurant_id>/newMenuItem/')
def newMenuItem(restaurant_id):
    return 'New Menu Item'


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return 'edit menu item'


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return 'delet menu item'


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
