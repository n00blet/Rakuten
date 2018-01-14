# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from rakuten.items import *


class PavithraSpider(CrawlSpider):
	name = "rakuten_spider"
	allowed_domains = ['rakuten.co.jp']
	start_urls = ['https://search.rakuten.co.jp/search/mall/handbags/']

	def parse(self, response):
		sel = Selector(response)
		handbags = sel.xpath('//div[@class="rsrSResultItemTxt"]/h2/a/@href').extract()
		print len(handbags)
		no_url = "#ITEMURL#"
		for i in range(len(handbags)):
			if no_url not in handbags[i]:    			
				yield Request(handbags[i],callback=self.parse_each)
				
			
	   
	def parse_each(self,response):    	
		sel = Selector(response)    	
		price = sel.xpath('//span[@class="price2"]/@content').extract()    	
		dollars = 112842
		items = []
		item = RakutenItem()
		if len(price)>=1 and int(price[0])>dollars:    		   		    	
			item['handbag_url'] = response.url
			item['handbag_price'] = int(price[0])
			handbag_image_urls = sel.xpath("//table[4]/tr/td[1]/a/img/@src").extract()
			handbag_brand = sel.xpath("//table[@class='tblitemspec']/tr[2]/td/text()").extract()[0].encode('ascii', errors='ignore')    		
			if not handbag_image_urls:
				item['handbag_image_urls'] = "not available"
			else:
				item['handbag_image_urls'] = handbag_image_urls

			if not handbag_brand:
				item['handbag_brand'] = "not available"
			else:
				item['handbag_brand'] = handbag_brand
		items.append(item)    		
		return items


