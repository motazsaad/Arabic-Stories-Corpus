from newspaper import Article
from newsplease import NewsPlease
import json

urls = open('mawdoo3_stories_urls.txt', encoding='utf-8').read().split('\n')
out = open('mawdoo3_stories.txt', mode='w', encoding='utf-8')
for url in urls:
    try:
        article = NewsPlease.from_url(url)
        print(article.title)
        out.write(article.title + '\n')
        out.write(article.text + '\n\n')
    except BaseException as error:
        print('ERROR: {}'.format(error))
