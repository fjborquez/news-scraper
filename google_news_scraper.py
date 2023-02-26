import uuid
import logging

from gnews import GNews

import news_persistence_client
from news_analyzer_client import search_companies

TOPICS = ['WORLD']
PERIOD = '1h'
gnews_client = GNews(period=PERIOD)
logging.basicConfig(filename="log.txt", level=logging.DEBUG)


def main():
    logging.debug("Init scraper task")
    news = get_news()
    print("Init send to api task")
    send_to_api(news)
    logging.debug("Finishing scraper task")


def get_news():
    news = []

    for topic in TOPICS:
        for a_news in gnews_client.get_news_by_topic(topic):
            complete_news_data(a_news, topic)
            news.append(a_news)

    return news


def complete_news_data(news, topic):
    news["topic"] = topic
    news["full_article"] = get_full_article(news)
    news["companies"] = get_companies(news)


def get_full_article(news):
    try:
        full_article = gnews_client.get_full_article(news["url"]).text
    except:
        full_article = ''

    return full_article


def send_to_api(news):
    for a_news in news:
        news_to_send = {
            'title': a_news['title'],
            'body': a_news['full_article'],
            'date': a_news['published date'],
            'url': a_news['url'],
            'site': {
                'url': a_news['publisher']['href'],
                'name': a_news['publisher']['title'],
            },
            'companies': a_news['companies']
        }

        news_persistence_client.send_to_api(news_to_send)


def get_companies(news):
    return search_companies(news)


main()
