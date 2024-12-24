import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class DetailsSpider(CrawlSpider):
    name = "details"
    allowed_domains = ["understat.com"]
    base_url = "https://understat.com/player/{}"

    current_id = 13284

    def start_requests(self):
        yield scrapy.Request(
            self.base_url.format(self.current_id),
            callback=self.parse_player,
            errback=self.handle_error,
            dont_filter=True,
        )

    def parse_player(self, response):
        if "Page not found" in response.text:
            self.logger.info(f"Player ID {self.current_id} not found. Skipping...")
        else:
            player_id = response.url.split("/")[-1]
            player_details = response.css("ul.breadcrumb")

            for p in player_details:
                yield {
                    "player_id": player_id,
                    "name": p.css("li::text").get(),
                    "league": p.css('a[href*="league/"]::text').get(),
                }

        self.current_id += 1
        yield scrapy.Request(
            self.base_url.format(self.current_id),
            callback=self.parse_player,
            errback=self.handle_error,
            dont_filter=True,
        )

    def handle_error(self, failure):
        self.logger.info(
            f"Error processing player ID {self.current_id}: {repr(failure)}"
        )
        self.current_id += 1
        yield scrapy.Request(
            self.base_url.format(self.current_id),
            callback=self.parse_player,
            errback=self.handle_error,
            dont_filter=True,
        )
