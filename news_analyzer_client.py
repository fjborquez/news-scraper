from analyzer import analyze


def search_companies(news):
    companies = analyze(news)

    if len(companies) > 0:
        news['companies'] = companies
