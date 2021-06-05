
from os import name
from app import app
import urllib.request,json
from app.models import source

Source = source.Source

#Getting api key
api_key = app.config['NEWS_API_KEY']
#Getting the news base url
base_url = app.config['NEWS_SOURCES_API_BASE_URL']


def get_sources(category):
    '''
    Function that gets the jso response to our url request
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
        
        
        
        
    