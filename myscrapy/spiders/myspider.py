# encoding=utf8
import chardet
import scrapy
from myscrapy.items import MyscrapyItem


class DmozSpider(scrapy.Spider):
    name = "qiubai"
    start_urls = [
        "http://www.8mxs.cc/read.asp?id=44977"
    ]

    def parse(self, response):
        qiubai = MyscrapyItem()
        # print 'start $$$$$$$$$$$$$$$$$$$$$$$'
        # print response.xpath('//div[@class="bai"]/a/@href|//div[@class="du"]/a/@href').extract()
        # print 'end $$$$$$$$$$$$$$$$$$$$$$$'
        a = 0
        for item in response.xpath('//div[@class="bai"]/a/@href|//div[@class="du"]/a/@href').extract():
            if a > 1:
                break
            a = a + 1
            yield scrapy.Request(url=item, callback=self.second_parse)

    # 对于返回的小类url，再进行递归请求
    def second_parse(self, response):
        print response.xpath('//title/text()')[0].extract().encode('utf-8').decode('utf-8')
        for item in response.xpath('//td[@class="content"]/text()'):
            print item.extract().encode('utf-8').decode('utf-8')

# for item in response.xpath('/html/body/div[@id="content"]/div/div[1]/div'):
#     name = item.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract()
#     if name:
#         qiubai['name'] = name[0]
#     news_id= item.xpath('./div[@class="author clearfix"]/a[1]/@href').extract()
#     if news_id:
#         qiubai['news_id']=news_id[0]
#
#     url = item.xpath('./a[@class="contentHerf"]/@href').extract()
#     if url:
#         qiubai['url'] = url[0]
#
#     text_content = item.xpath('./a[@class="contentHerf"]/div/span/text()').extract()
#     if text_content:
#         qiubai['text_content'] = text_content[0]
#
#     has_image = item.xpath('./div[@class="thumb"]/a/img[@src]').extract()
#     if has_image:
#         qiubai['has_image'] = '1'
#     else:
#         qiubai['has_image'] = '0'
#
#     yield qiubai
