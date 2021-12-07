from timecoverspider.items import MagazineCover
import datetime
import scrapy
class CoverSpider(scrapy.Spider):
	name = "pyimagesearch-cover-spider"
	start_urls = ["http://search.time.com/results.html?N=46&Ns=p_date_range|1"]
	def parse(self, response):
		# let's only gather Time U.S. magazine covers
		url = response.css("div.refineCol ul li").xpath("a[contains(., 'TIME U.S.')]")
		yield scrapy.Request(url.xpath("@href").extract_first(), self.parse_page)


def parse_page(self, response):
    for href in response.xpath("//a[contains(., 'Large Cover')]"):
        yield scrapy.Request(href.xpath("@href").extract_first(),
                             self.parse_covers)
    next = response.css("div.pages").xpath("a[contains(., 'Next')]")
    yield scrapy.Request(next.xpath("@href").extract_first(), self.parse_page)

def parse_covers(self, response):
		img = response.css(".art-cover-photo figure a img").xpath("@src")
		imageURL = img.extract_first()
		title = response.css(".content-main-aside h1::text").extract_first()
		year = response.css(".content-main-aside h1 time a::text").extract_first()
		month = response.css(".content-main-aside h1 time::text").extract_first()[:-2]
		date = "{} {}".format(month, year).replace(".", "")
		d = datetime.datetime.strptime(date, "%b %d %Y")
		pub = "{}-{}-{}".format(d.year, str(d.month).zfill(2), str(d.day).zfill(2))
		yield MagazineCover(title=title, pubDate=pub, file_urls=[imageURL])