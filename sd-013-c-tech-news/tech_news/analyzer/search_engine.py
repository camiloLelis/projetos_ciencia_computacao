from tech_news.database import search_news
from datetime import datetime
import re


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    # ref: https://stackoverflow.com/questions/6266555/
    # querying-mongodb-via-pymongo-in-case-insensitive-efficiently
    result = search_news({'title': re.compile(title, re.IGNORECASE)})
    return [(item["title"], item["url"]) for item in result]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    # ref: https://pt.stackoverflow.com/questions/377579/
    # valida%C3%A7%C3%A3o-de-data-testes-com-python
    try:
        if datetime.strptime(date, "%Y-%m-%d"):
            # ref regex: https://github.com/tryber/sd-013-c-tech-news/
            # blob/Amos-Rodrigues-tech-news/tech_news/analyzer/search_engine.py
            result = search_news({"timestamp": {"$regex": date}})
            return [(item["title"], item["url"]) for item in result]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    result = search_news({"sources": {
        "$all": [re.compile(
            source, re.IGNORECASE)]}}
        )
    return [(item["title"], item["url"]) for item in result]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    result = search_news({"categories": {
        "$all": [re.compile(
            category, re.IGNORECASE)]}}
        )
    return [(item["title"], item["url"]) for item in result]
