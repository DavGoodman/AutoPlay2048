# Automatically opens and plays the 2048 game in browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('https://play2048.co/')
html_elem = browser.find_element_by_tag_name("html")

while True:
    html_elem.send_keys(Keys.ARROW_DOWN)
    html_elem.send_keys(Keys.ARROW_LEFT)
    html_elem.send_keys(Keys.ARROW_UP)
    html_elem.send_keys(Keys.ARROW_RIGHT)
