from analyzer import analyze


def search_companies(news):
    companies = analyze(news["full_article"])

    if len(companies) > 0:
        return companies
    else:
        return []