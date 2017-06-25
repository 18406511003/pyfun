# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



#
# import requests
# import sys,os
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# #用requests的get方法获取图片并保存入文件
# class MeizituPipeline(object):
#     def process_item(self, item, spider):
#         pic_url=item['pic_url']
#
#
#         image=requests.get(pic_url)
#         f=open('D:\pycharm\meizitu','wb')
#         f.write(image.content)
#         f.close()
#
#         return item




# import requests
# import os
#
# # 图片下载类
# class MeizituPipeline(object):
#     def process_item(self, item, spider):
#         if 'pic_url' in item:  # 如何‘图片地址’在项目中
#             images = []  # 定义图片空集
#             dir_path = 'F:\meizitu'
#             if not os.path.exists(dir_path):
#                 os.makedirs(dir_path)
#             for image_url in item['pic_url']:
#                 for i in range(100):
#                 # us = image_url.split('/')[3:]
#                     image_file_name = 'i'
#                 file_path = '%s/%s' % (dir_path, image_file_name)
#                 images.append(file_path)
#                 if os.path.exists(file_path):
#                     continue

# import json,codecs
#
# class MeizituPipeline(object):
#     def __init__(self):
#         self.file = codecs.open('meizitu_utf-8.json', 'wb', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item)) + '\n'
#         # print line
#         self.file.write(line.decode("unicode_escape"))

# import requests,os
# class MeizituPipeline(object):
#     def process_item(self, item, spider):
#         pic_url = item['pic_url']
#         title = item ['title']
#         image = requests.get(pic_url)
#         dir_path = 'F:\meizitu'
#         if not os.path.exists(dir_path):
#             os.makedirs(dir_path)
#         for i in range(100):
#             with open('i', 'wb') as dir_path:
#                 dir_path.write(image.content)
#                 dir_path.close()
#
#         return item

import os
import urllib,requests

from meizitu import settings


class MeizituPipeline(object):
    def process_item(self, item, spider):
        dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)  # 存储路径
        print 'dir_path', dir_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for image_url in item['pic_url']:
            list_name = image_url.split('/')
            print list_name
            file_name = list_name[len(list_name) - 1]  # 图片名称
            # print 'filename',file_name
            file_path = '%s/%s' % (dir_path, file_name)
            # print 'file_path',file_path
            # if os.path.exists(file_name):
            #     continue
            with open(file_path, 'wb') as file_writer:
                conn = requests.get(image_url)  # 下载图片
                file_writer.write(conn.content)
            file_writer.close()
        return item

