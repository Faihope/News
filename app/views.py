from app.request import get_sources
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
