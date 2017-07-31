import os
import scrapy

PORT = os.environ.get('PORT', '80')

class LocalSiteSpider(scrapy.Spider):
    name = 'Local Site Spider'
    start_urls = ['http://localhost:' + PORT]

    def parse(self, response):
        targets = response.xpath('//*[@id]/@id').extract() + response.xpath('//a[@name]/@name').extract()
        for link in response.xpath('//a[@href]'):
            href = link.xpath("@href").extract_first()
            if href is None or href.startswith("mailto:") or href.startswith("http") or href.endswith(".zip") or href == "#":
                pass
            elif href.startswith("#"):
                if href[1:] not in targets:
                    yield {"error": "internal-link-not-found", "msg": "Expected target " + href + " but not found on page " + response.url}
            else:
                yield response.follow(link, self.parse)
