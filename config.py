import os

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY')
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey={}'
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
