# ref: https://www.w3schools.com/python/ref_string_strip.asp
# Requisito 1 pr
import time
import requests
from parsel import Selector
from tech_news.database import create_news


def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    response = []
    classe = "h3 .tec--card__title__link"
    """ response = a(selector.css("a::attr(href)").get()) """
    for div in selector.css(classe):
        response.append(div.xpath('.//@href').get())
    return response


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css('div.tec--list > a::attr(href)').get()


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    retorno = {}

    retorno["url"] = selector.css('link[rel="canonical"]::attr(href)').get()
    retorno["title"] = selector.css('.tec--article__header__title::text').get()
    retorno["timestamp"] = selector.css(
                                '#js-article-date::attr(datetime)'
                            ).get()
    retorno["writer"] = (
            selector.css(
                "div.tec--author__info p.z--m-none:first-child *::text"
            ).get()
            or selector.css(
                "div.tec--timestamp div.tec--timestamp__item a::text"
            ).get()
        ).strip()
    retorno["shares_count"] = int(selector.css(
                                    '.tec--toolbar__item::text'
                                ).re_first(r'\d+') or 0)
    retorno["comments_count"] = int(selector.css(
                                    '#js-comments-btn::text'
                                    ).re_first(r'\d+')) if not None else 0
    retorno["summary"] = ''.join(selector.css(
                        '.tec--article__body > p:nth-child(1) *::text'
                                    ).getall()) or None
    retorno["sources"] = [cat.strip() for cat in selector.css(
        '.z--mb-16 .tec--badge::text'
                ).getall()]

    retorno["categories"] = [cat.strip() for cat in selector.css(
        '#js-categories > a::text'
                ).getall()]

    return retorno


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    base = "https://www.tecmundo.com.br/novidades"
    contentSite = fetch(base)
    linkNews = scrape_novidades(contentSite)
    arrayNews = []
    while(amount > len(linkNews)):
        contentSite = fetch(scrape_next_page_link(contentSite))
        linkNews.extend(scrape_novidades(contentSite))

    del(linkNews[amount:])
    for link in linkNews:
        page = fetch(link)
        newsObj = scrape_noticia(page)
        arrayNews.append(newsObj)

    create_news(arrayNews)
    return arrayNews
