from pprint import pprint

from gnews import GNews

TOPICS = ['WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY', 'ENTERTAINMENT', 'SPORTS', 'SCIENCE', 'HEALTH']
PERIOD = '2h'
gnews_client = GNews(period=PERIOD)


def main():
    news = get_news()
    set_full_article(news)
    send_to_api(news)
    pprint(news)


def get_news():
    read = []

    for topic in TOPICS:
        read += gnews_client.get_news_by_topic(topic)

    return read


def set_full_article(news):
    for a_news in news:
        try:
            a_news['full_article'] = gnews_client.get_full_article(a_news['url']).text
        except:
            a_news['full_article'] = ''


def send_to_api(news):
    return ""


main()
