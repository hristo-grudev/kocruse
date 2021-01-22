import scrapy
from scrapy.exceptions import CloseSpider

from scrapy.loader import ItemLoader
import re

from w3lib.html import remove_tags

from ..items import KocruseItem


class KocruseSpider(scrapy.Spider):
	name = 'kocruse'
	start_urls = ['https://kocruse.com/preparing-delivering-food/']
	page = 0

	def parse(self, response):
		yield self.parse_post(response)

		pagination_links = response.xpath('//h4[@class="nbs nsNext"]/a/@href')
		yield from response.follow_all(pagination_links, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h2/span[@class="headline"]/text()').get()
		description = response.xpath('//article/div/div/div[2]|//article/div/div/div[3]').getall()

		description = (remove_tags(''.join(description))).strip()
		date = response.xpath('//div[@class="btSubTitle"]/span/text()').get()
		date = date.strip()

		item = ItemLoader(item=KocruseItem(), response=response)
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)
		print(date)

		return item.load_item()
