from app import app
import urllib.request,json
from .models import article
from .models import source
Source=source.Source
Article=article.Article

# getting  api key
api_key= app.config['NEWS_API_KEY']

# getting the article base url
source_url=app.config['SOURCE_API_BASE_URL']
base_url=app.config['ARTICLE_API_BASE_URL']

def get_source():
    '''
    function that gets the sources
    '''

    with urllib.request.urlopen(source_url) as url:
        get_source_data=url.read()
        get_source_response=json.loads(get_source_data)

        source_results=None

        if get_source_response['sources']:
            source_results_list=get_source_response['sources']
            source_results=process_results(source_results_list)
    return source_results

def get_articles(source):
    '''
    function that gets articles for a particular source
    args: source
    return: articles for that source
    '''
    get_articles_url= base_url.format(source,api_key)
    print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data=url.read()
        get_articles_response=json.loads(get_articles_data)

        article_results=None

        if get_articles_response['articles']:
            article_results_list=get_articles_response['articles']
            article_results=process_articles(article_results_list)

    return article_results

def process_articles(article_list):
    '''
    function that processthe results and turn them to a list
    args:
        article_list: a list from the api
    returns:
        article_results: a list of source objects
    '''

    article_results=[]
    for article_item in article_list:
        author=article_item.get('author')
        title=article_item.get('title')
        description=article_item.get('description')
        url=article_item.get('url')
        image=article_item.get('urlToImage')
        date=article_item.get('date')


        article_object=Article(author,title,description,url,image,date)
        article_results.append(article_object)

    return article_results


def process_results(source_list):
    '''
    function that processthe results and turn them to a list
    args:
        source_list: a list from the api
    returns:
        source_results: a list of source objects
    '''

    source_results=[]
    for source_item in source_list:
        id=source_item.get('id')
        name=source_item.get('name')
        description=source_item.get('description')
        url=source_item.get('url')
        category=source_item.get('category')

        source_object=Source(id,name,description,url,category)
        source_results.append(source_object)

    return source_results
