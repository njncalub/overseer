import scrapy

# Update the settings below to fetch the data that you want. For more
# information, you can check the tutorials at:
# https://docs.scrapy.org/en/latest/intro/tutorial.html
BASE_URL = "http://structured-novel-site.com/novel/chapter-"
BODY_SELECTOR = ".body-selector"
TITLE_SELECTOR = ".title-selector ::text"
CONTENT_SELECTOR = ".content-selector ::text"

# Hard-coding what pages we start and end with. This only works if the pages are
# structured correctly. If not, update the logic in your code.
# TODO(njncalub): Add these as optional command-line arguments, defaulting to 0.
START_PAGE = 0
LAST_PAGE = 0


class StructuredSiteSpider(scrapy.Spider):
    """Scraper for a structured novel hosting site."""

    name = "structured-novel-site"
    page = START_PAGE
    start_urls = [f"{BASE_URL}{page}"]

    def parse(self, response):
        for body in response.css(BODY_SELECTOR):
            yield {
                "url": f"{BASE_URL}{self.page}",
                "chapter": self.page,
                "title": body.css(TITLE_SELECTOR).extract_first(),
                "content": "\n".join(body.css(CONTENT_SELECTOR).extract()),
            }

        self.page += 1
        if self.page <= LAST_PAGE:
            yield response.follow(f"{BASE_URL}{self.page}", self.parse)
