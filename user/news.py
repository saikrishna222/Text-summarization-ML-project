from newspaper import Article
def downloadwebpage(url):
    # downloads the whole webpage
    article = Article(url)
    article.download()

    # parses the downloaded html
    article.parse()
    text = article.text
    return text