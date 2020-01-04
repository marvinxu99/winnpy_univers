from selenium import webdriver

browser = webdriver.Chrome('.\chromedriver')

# browser.get('http://seleniumhq.org/')
# browser.close()

browser.maximize_window()
browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in browser.title

show_message_button = browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))

# Python selenium commands cheat sheet
# http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/

assert "Show Message" in browser.page_source   # page source is the page html

user_message = browser.find_element_by_id('user-message')
user_message.clear()  # clear the input box
user_message.send_keys('I AM Extra coool')

show_message_button.click()

output_message = browser.find_element_by_id('display')

assert 'I AM Extra coool' in output_message.text

user_button = browser.find_elements_by_css_selector('#get-input > .btn')
print(user_button)

# browser.close()

#browser.quit()   # quit the browser driver (will close all instances)
