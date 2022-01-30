"""
import os

class Config:

    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey={}'

    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_API_KEY = 2916d5e6b1384e98b9e5cf5822356016('NEWS_API_KEY')
    

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
"""