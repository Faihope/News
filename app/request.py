
from flask.blueprints import DeferredSetupFunction
from app.models.articles import Articles
from os import name
from app import app
import urllib.request,json
from app.models import source,articles
from datetime import datetime


Source = source.Source
Articles = articles.Articles

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config['NEWS_SOURCES_API_BASE_URL']
#Getting the articles url
articles_url = app.config['ARTICLES_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        source_results = None
        
        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)
            
    return source_results

def process_results(source_list):
    '''
    Function that processes the source result and transform them to a list of Objects
    Args:
        sources_list:A list of dictionaries that contain news details
    Returns:
            source_results:A list of news objects  
    '''
    
    source_results=[] 
    for source_item in  source_list:
        id = source_item.get('id') 
        name= source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
     
  
        sources_object = Source(id,name,description,url,category,country,language)
        source_results.append(sources_object)
        
    return source_results


def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = articles_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        articles_results = None
        
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
            
    return articles_results

def process_articles(articles_list):
    '''
     Function that processes the articles result and transform them to a list of Objects
    Args:
        articles_list:A list of dictionaries that contain articles details
    Returns:
           articles_result:A list of articles objects  
    '''
    
    articles_object = []
    for article_item in articles_list:
        id=article_item.get('id')
        author=article_item.get('author')
        title=article_item.get('title')
        description=article_item.get('description')
        url=article_item.get('url')
        image=article_item.get('urlToImage')
        date=article_item.get('publishedAt')
        
        
        if image:
            articles_result =Articles(id,author,title,description,url,image,date)
            articles_object.append(articles_result)
    print(articles_object)
    return articles_object
    
    
    
        
        
        
        
    