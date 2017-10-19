from flask import render_template
from app import app
from .request import get_source,get_articles

@app.route('/')
def index():
    '''
    view root page
    '''

    # getting sources
    sources=get_source()
    cnn=get_articles('bbc-sport')
    # print(sources)
    trunc=cnn[0:4]
    title='Home - Where you can find all your latest news in one website'
    return render_template('index.html' ,title=title,sources=sources,cnn=trunc)

@app.route('/source/<source_name>')
def source(source_name):
    '''
    view articles for a source
    '''
    render_template('source.html',name = source_name)
