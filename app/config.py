class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_BASE_URL='https://newsapi.org/v1/sources?language=en'
    ARTICLE_API_BASE_URL='https://newsapi.org/v1/articles?source={}&sortBy=top&apiKey={}'
    CATEGORY_API_BASE_URL="https://newsapi.org/v1/sources?language=en&category={}"



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
