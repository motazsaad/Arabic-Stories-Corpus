import newspaper

# web_url = 'https://www.hikayatatfal.com/'
web_url = 'https://www.qisasse.com/'
stories = {}
urls = [
    'https://www.qisasse.com/',
    'https://storiestales.com/',
    'https://www.storiesrealistic.com/',
    'https://www.hikayatatfal.com/'
]
for web_url in urls:
    print(web_url)
    stories_site = newspaper.build(web_url)
    print(stories_site.articles)
# for article in stories_site.articles:
#     article.download()
#     article.parse()
#     print(article.title)
#     stories[article.url] = {'title': article.title,
#                             'text': article.text}
#     print(stories_site)
