from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import Product
from . import db


productPage = Blueprint('productPage', __name__)

@productPage.route('/products', methods=['GET'])
def display_products():
    products_names = []
    products = Product.query.all()
    for product in products:
        products_names.append(product.name)
    return render_template('product.html', products=products_names)


@productPage.route('/products/add_product')
def signup():
    return render_template('add_products.html')


@productPage.route('/products/add_product', methods=['POST'])
def add_product():
    name = request.form.get('name')
    price = request.form.get('price')

    product = Product.query.filter_by(name=name).first() # if this returns a user, then the email already exists in database

    if product:
        flash('Product already exists')
        return redirect(url_for('productPage.add_product'))

    new_product = Product(name=name, price=price)

    db.session.add(new_product)
    db.session.commit()

    return redirect(url_for('productPage.products'))
