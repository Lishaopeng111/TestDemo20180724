# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 14:37
# @Author  : Lsp

# import requests
# res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# print(type(res))
# print(requests.codes.ok)
# print(res.status_code)
# print(res.cookies)
# print(len(res.text))
# playFile = open('RomeoAndJuliet.txt', 'r+',encoding='utf-8')
# playFile.write(res.text)

import requests
from bs4 import BeautifulSoup

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
res = requests.get('http://jandan.net/ooxx', headers=headers)
soup = BeautifulSoup(res.text.strip('<img>'), 'html.parser')
# example = soup.find_all('em')

example = soup('src')
print(example)
# with open(r'1.txt','w+',encoding='utf8') as f:
# 	for i in example:
# 		i=str(i)
# 		i=i.strip('<em>').strip('</em>').strip('商品筛选 -').strip('上一页共<b>161</b>页  到第页id="copyright_year">2018').lstrip('\n').strip('                                    ')
# 		f.write(i)
# f.close()
# with open(r'1.txt','r+',encoding='utf8')as f:
# 	for i in f.readline():
# 		print(i,end='')
