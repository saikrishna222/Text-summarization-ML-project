
# for scraping the webpage
from newspaper import Article

# for removing square brackets
import re

# Gensim summarizer
from gensim.summarization.summarizer import summarize

# For extracting the keywords
from gensim.summarization import keywords

# downloads the article and parses the html, uses lxml parser

from user.news import downloadwebpage

def sum_it_up(url):

    content = downloadwebpage(url)
    len_content=len(content.split())
    # remove the reference numbers
    re.sub(r'\[.+\]', '', content)

    # finds a list of 10 important keywords, usses lemmetatization instead of stemming
    k = keywords(content, words=20, lemmatize=True).split('\n')
    kwords = ', '.join(k)

    # computes summary and reduces size by 20%
    return(summarize(content), kwords,len_content)
