from flask import render_template
from app import app
from .request import get_sources,get_articles

@app.route('/')
def index():
    '''
    view root page
    '''

    # getting sources
    sources=get_sources()
    cnn=(get_articles('cnn'))[0:4]
    bbc_sport=(get_articles('bbc-sport'))[0:4]
    techcrunch=(get_articles('TechCrunch'))[0:4]
    # print(sources)
    title='Home - Where you can find all your latest news in one website'
    return render_template('index.html' ,title=title,sources=sources,cnn=cnn ,bbc_sport=bbc_sport,techcrunch=techcrunch)

@app.route('/source/<source_id>')
def source(source_id):
    '''
    view articles for a source
    '''

    source=get_articles(source_id)

    return render_template('source.html',source = source)

# @app.route('/')
# def asdf():
#     render_template('source.html')
