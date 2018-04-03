# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: shiyanlou_courses_spider.py 
@time: 2018/04/03 
"""
import scrapy


class ShiyanlouCoursesSpider(scrapy.Spider):
    # """ 所有 scrapy 爬虫需要写一个 Spider 类，这个类要继承 scrapy.Spider 类。在这个类中定义要请求的网站和链接、如何从返回的网页提取数据等等。
    # """

    # 爬虫标识符号，在 scrapy 项目中可能会有多个爬虫，name 用于标识每个爬虫，不能相同
    name = 'shiyanlou-courses'

    def start_requests(self):
        # """ 需要返回一个可迭代的对象，迭代的元素是 `scrapy.Request` 对象，可迭代对象可以是一个列表或者迭代器，这样 scrapy 就知道有哪些网页需要爬取了。`scrapy.Request` 接受一个 url 参数和一个 callback 参数，url 指明要爬取的网页，callback 是一个回调函数用于处理返回的网页，通常是一个提取数据的 parse 函数。
        # """
        url_template = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=Python&unfold={}'
        urls = (url_template.format(i) for i in range(1, 8))
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):
        # """ 这个方法作为 `scrapy.Request` 的 callback，在里面编写提取数据的代码。scrapy 中的下载器会下载 `start_reqeusts` 中定义的每个 `Request` 并且结果封装为一个 response 对象传入这个方法。
        # """
        for course in response.xpath('//a[@class="course-box"]'):
            yield {
                'name': course.xpath('.//div[@class="course-name"]/text()').extract_first(),
                'desc': course.xpath('.//div[@class="course-desc"]/text()').extract_first(),
                'students': course.xpath('.//span[contains(@class,"course-per-num")]/text()').re_first('[^\d](\d)*[\d$]')
            }


if __name__ == '__main__':
    shiyanlou_spider = ShiyanlouCoursesSpider()
    shiyanlou_spider.start_requests()