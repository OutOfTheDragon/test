__author__ = 'User'

from selenium import webdriver
import os

def Chrome_driver():
    chrome_driver = os.path.abspath('C:\Users\User\IdeaProjects\\test\chromedriver.exe')
    os.environ['webdriver.chrome.driver'] = chrome_driver
    return chrome_driver

def IE_driver():
    ie_driver = os.path.abspath('C:\Users\User\IdeaProjects\\test\IEDriverServer.exe')
    os.environ['webdriver.ie.driver'] = ie_driver
    return ie_driver