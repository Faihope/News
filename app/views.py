from app.request import get_sources,get_articles,process_articles,process_results
from flask import render_template,request
from app import app
from .models import articles,source

#Views

@app.route('/')
def index():
    '''
    Page that returns index page and its data
    '''
    
    sources = get_sources('sources')
    welcome = 'Welcome to News App'
    return render_template('index.html',welcome=welcome,sources= sources)
@app.route('/articles')
def articles():
    '''
    articles function that views articles page
    '''
    articles = get_articles('technology')
    
    title = f'NH | {id}'
    
    return render_template('articles.html',articles=articles,title=title)

@app.route('/technology')
def technology():
    '''
    articles function that views articles page
    '''
    articles = get_articles('technology')
    
    title = f'NH | {id}'
    
    return render_template('articles.html',articles=articles,title=title)
    
@app.route('/business')
def business():
    '''
    articles function that views articles page
    '''
    articles = get_articles('business')
    
    title = f'NH | {id}'
    
    return render_template('articles.html',articles=articles,title=title)
    