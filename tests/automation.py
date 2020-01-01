from selenium import webdriver

browser = webdriver.Chrome('.\chromedriver')

browser.get('http://seleniumhq.org/')

browser.maximize_window()
