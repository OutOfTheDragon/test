__author__ = 'User'
# -*- coding:utf-8 -*-
import selenium
from selenium import  webdriver
from driver_config import Chrome_driver


driver = webdriver.Chrome(Chrome_driver())
driver.get('http://www.baidu.com')
driver.maximize_window()
