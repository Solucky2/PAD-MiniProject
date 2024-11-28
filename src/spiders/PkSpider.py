from typing import Any
import scrapy
from scrapy.http import Response


class PkSpider(scrapy.Spider):
    name = 'PkSpider'
    pk_pages_num = 29
    start_urls = [f'https://www.przyjacielekawy.pl/c/kawa/page/{i}/' for i in range(1, pk_pages_num + 1)]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        products = response.css("ul.products li.product")
        for product in products:
            yield self._parse_products(product)

    def _parse_products(self, product: Response) -> dict:
        item = {
            "name": product.css("h2.woocommerce-loop-product__title::text").get(default="N/A"),
            "price_old": product.css("del span.woocommerce-Price-amount bdi::text").re_first(r"\d+,\d+", default="N/A"),
            "price_new": product.css("ins span.woocommerce-Price-amount bdi::text").re_first(r"\d+,\d+", default="N/A")
        }
        return item
