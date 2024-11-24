from typing import Any
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response


class KonessoSpider(scrapy.Spider):
    name = "KonessoSpider"
    konesso_pages = 86
    start_urls = [f"https://www.konesso.pl/pol_m_Kawa-2147.html?counter={i}" for i in range(1, konesso_pages + 1)] #git


    def parse(self, response: Response, **kwargs: Any) -> Any:
        products = response.css("div.product_wrapper")
        for product in products:
            yield self._parse_products(product)


    def _parse_products(self, product: Response) -> dict:
        item = {
            "name": product.css("a.name h5::text").get(default="N/A").strip(),
            "price_old": product.css("div.product_prices span del.max-price::text").get(default="N/A").strip(),
            "price_netto": product.css("div.product_prices span.price .price-netto::text").get(default="N/A").strip(),
            "price_new": product.css("div.product_prices span.price::text").re_first(r"\d+,\d+\s?zł", default="N/A")
        }
        return item

process = CrawlerProcess(settings={
    "FEEDS": {
        "scrapped_pages/output_konesso.csv": {"format": "csv"},
    },
})
process.crawl(KonessoSpider)
process.start()
