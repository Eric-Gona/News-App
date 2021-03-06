from flask import render_template,request,redirect,url_for
from ..requests import getSources, get_articles
from ..models import Source
from . import main

@main.route('/')
def index():
    
    newsapi = NewsApiClient (api_key='2916d5e6b1384e98b9e5cf5822356016')
    news = getSources()

    title = 'Highlights'

    return render_template('index.html',title = title, news = news)

@main.route('/entertainment/')
def entertainment():
    
    entertainment = get_articles("entertainment")

    title = 'Entertainment'

    return render_template('entertainment.html',title = title, entertainment = entertainment)

@main.route('/business/')
def business():
    
    business = get_articles("business")

    title = 'Business'

    return render_template('business.html',title = title, business = business)

