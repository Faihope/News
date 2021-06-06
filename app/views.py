from app.request import get_sources,get_articles
from flask import render_template
from app import app

#Views

@app.route('/')
def index():
    '''
    Page that returns index page and its data
    '''
    
    sources = get_sources('sources')
  
    print(sources)
    welcome = 'Welcome to News App'
    return render_template('index.html',welcome=welcome,sources= sources)
@app.route('/sources/<int:articles_id>')
def articles(articles_id):
    '''
    articles function that views articles page
    '''
    articles = get_articles(id)
    title = f'NH | {id}'
    
    return render_template('articles.html',id=articles_id,articles=articles,title=title)
    
