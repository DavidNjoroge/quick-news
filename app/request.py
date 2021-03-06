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
category_url=app.config['CATEGORY_API_BASE_URL']

def get_sources():
    '''
    function that gets the sources
    '''

    with urllib.request.urlopen(source_url) as url:

        print(url)
        get_source_data=url.read()

        # print(get_source_data)
        get_source_response=json.loads(get_source_data)

        # print(get_source_response)

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
    # print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data=url.read()
        get_articles_response=json.loads(get_articles_data)

        article_results=None

        if get_articles_response['articles']:
            source=get_articles_response['source']

            article_results_list=get_articles_response['articles']
            article_results=process_articles(article_results_list,source)

    return article_results

def get_category(category):
    get_category_url=category_url.format(category)

    with urllib.request.urlopen(get_category_url) as url:
        get_category_data=url.read()
        get_category_response=json.loads(get_category_data)

        category_results=None

        if get_category_response['sources']:
            category_results_list=get_category_response['sources']
            category_results=process_results(category_results_list)


    return category_results

def process_articles(article_list,source_name):
    '''
    function that processthe results and turn them to a list
    args:
        article_list: a list from the api
    returns:
        article_results: a list of source objects
    '''

    article_results=[]
    for article_item in article_list:
        source=source_name
        author=article_item.get('author')
        title=article_item.get('title')
        description=article_item.get('description')
        url=article_item.get('url')
        image=article_item.get('urlToImage')
        date=article_item.get('date')


        article_object=Article(author,title,description,url,image,date,source)
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

	# print(source_results)

    # print(len(source_results))
    return source_results
def process_category(category_list):
    # print(len(category_list))
    category_processed=[]
    if len(category_list)>=4:
        temp_category=category_list[0:4]
        for category in temp_category:
            source=(get_articles(category.id))[0:4]
            print(source[0].image)

            # category_item=get_articles(category.id)
            category_processed.append(source)
    else:
        for category in category_list:
            source=(get_articles(category.id))[0:4]
            print(source[0].image)

            # category_item=get_articles(category.id)
            category_processed.append(source)

    return category_processed
