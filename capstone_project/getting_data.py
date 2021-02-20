import os
from newsapi import NewsApiClient

# getting an api key from virtual environment and initialising
api_key = os.environ.get('NEWS_API')
newsapi = NewsApiClient(api_key=api_key)

# getting sources - 128 news websites
# id,name,description, url, category, language, country
sources = newsapi.get_sources()
news_agencies = sources['sources']


# getting headlines from sources:
# source, author, title, description, url, urlToImage, publishedAt, content
# random sources: axios, bild, google-news-it, news24, the-verge
top_headlines_bbc = newsapi.get_top_headlines(
                                          sources='bbc-news',
                                          language='en'
                                          )


top_headlines_ars = newsapi.get_top_headlines(
                                          sources='ars-technica',
                                          language='en'
                                          )

top_headlines_bild = newsapi.get_top_headlines(
                                          sources='bild',
                                          language='de'
                                          )

top_headlines_google = newsapi.get_top_headlines(
                                          sources='google-news-it',
                                          language='it'
                                          )

top_headlines_news24 = newsapi.get_top_headlines(
                                          sources='news24',
                                          language='en'
                                          )
top_headlines_verge = newsapi.get_top_headlines(
                                          sources='the-verge',
                                          language='en'
                                          )

bbc_headlines = top_headlines_bbc['articles']
ars_headlines = top_headlines_ars['articles']
bild_headlines = top_headlines_bild['articles']
google_headlines = top_headlines_google['articles']
news24_headlines = top_headlines_news24['articles']
verge_headlines = top_headlines_verge['articles']

# /v2/everything
# source, author, title, description, url, urlToImage,publishedAt, content
all_articles_bbc = newsapi.get_everything(
                                      sources='bbc-news',
                                      from_param='2021-02-14',
                                      to='2021-02-14',
                                      sort_by='relevancy')
all_articles_ars = newsapi.get_everything(
                                      sources='ars-technica',
                                      from_param='2021-02-14',
                                      to='2021-02-14',
                                      sort_by='relevancy')
all_articles_bild = newsapi.get_everything(
                                      sources='bild',
                                      from_param='2021-02-14',
                                      to='2021-02-14',
                                      sort_by='relevancy')
all_articles_google = newsapi.get_everything(
                                      sources='google-news-it',
                                      from_param='2021-02-14',
                                      to='2021-02-14',
                                      sort_by='relevancy')
all_articles_news24 = newsapi.get_everything(
                                      sources='news24',
                                      from_param='2021-02-14',
                                      to='2021-02-14',
                                      sort_by='relevancy')
all_articles_verge = newsapi.get_everything(
                                      sources='the-verge',
                                      from_param='2021-02-14',
                                      to='2021-02-14',
                                      sort_by='relevancy')

bbc_articles = all_articles_bbc['articles']
ars_articles = all_articles_ars['articles']
bild_articles = all_articles_bild['articles']
google_articles = all_articles_google['articles']
news24_articles = all_articles_news24['articles']
verge_articles = all_articles_verge['articles']