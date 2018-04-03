# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: shiyanlou_course_spider_1.py 
@time: 2018/04/03 
"""
import scrapy

class ShiyanlouCourseSpider(scrapy.Spider):

    name = 'shiyanlou_course_spider_1'

    @property
    def start_urls(self):
        url_template = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=Python&page={}'
        return (url_template.format(i) for i in range(1, 8))

    def parse(self, response):
        # """ 这个方法作为 `scrapy.Request` 的 callback，在里面编写提取数据的代码。scrapy 中的下载器会下载 `start_reqeusts` 中定义的每个 `Request` 并且结果封装为一个 response 对象传入这个方法。
        # """
        for course in response.xpath('//a[@class="course-box"]'):
            yield {
                'name': course.xpath('.//div[@class="course-name"]/text()').extract_first(),
                'desc': course.xpath('.//div[@class="course-desc"]/text()').extract_first(),
                'students': course.xpath('.//span[contains(@class,"course-per-num")]/text()').re_first('[^\d](\d)*[\d$]')
            }

