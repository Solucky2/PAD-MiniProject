from typing import Any

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response


class CoffeeCaveSpider(scrapy.Spider):
    name = "CoffeeCaveSpider"
    start_urls = [
        "https://coffeecave.pl/sklep/kawy-jednorodne" #git
    ]


    def parse(self, response: Response, **kwargs: Any) -> Any:
        products = response.css("div.main-product-box")
        for product in products:
            yield self._parse_product(product)


    def _parse_product(self, product: Response) -> dict:
        items = {
            "name": product.css("a.product-name::text").get(default="N/A").strip(),
            "price": product.css("div.price::text").get(default="N/A").strip()
        }
        return items
