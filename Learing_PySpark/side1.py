# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 11:46
# @Author  : Lsp
from selenium import webdriver

browser = webdriver.Chrome()
print(type(browser))
browser.get('http://jiandan.net/ooxx')
try:
	elem = browser.find_element_by_class_name('righttext')
	print('Found <%s> element with that class name!' % elem.tag_name)
except :
	print('Was not able to find an element with that name.')
