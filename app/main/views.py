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

