from app.request import get_sources,get_articles
from flask import render_template,request,redirect,url_for
from . import main


#Views

@main.route('/')
def index():
    '''
    Page that returns index page and its data
    '''
    
    sources = get_sources('sources')
    welcome = 'Welcome to News App'
    return render_template('index.html',welcome=welcome,sources= sources)
@main.route('/articles')
def articles():
    '''
    articles function that views articles page
    '''
    articles = get_articles('technology')
    
    title = f'NH | {id}'
    
    return render_template('articles.html',articles=articles,title=title)

@main.route('/technology')
def technology():
    '''
    articles function that views articles page
    '''
    articles = get_articles('technology')
    
    title = f'NH | {id}'
    
    return render_template('articles.html',articles=articles,title=title)
    
@main.route('/business')
def business():
    '''
    articles function that views articles page
    '''
    articles = get_articles('business')
    
    title = f'NH | {id}'
    
    return render_template('articles.html',articles=articles,title=title)
    
@main.route('/sports')
def sports():
    '''
    articles function that views articles page
    '''
    articles = get_articles('sports')
    
    title = f'NH | {id}'
    
    return render_template('articles.html',articles=articles,title=title)
    
