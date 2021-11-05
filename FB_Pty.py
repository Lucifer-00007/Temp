import selenium
from selenium import webdriver
import time
browser = webdriver.Edge("edgedriver.exe")

browser.get('https://fdown.net/')

VidUrl_field = browser.find_element_by_name('URLz')
VidUrl_field.clear()
VidUrl_field.send_keys('https://www.facebook.com/girlvideofp/videos/228967558585587/')

Down_button_next = browser.find_element_by_class_name("input-group-btn")
Down_button_next.click()

time.sleep(3)
Down_button = browser.find_element_by_id("sdlink")
Down_button.click()

# time.sleep(3)
# # browser.switch_to_alert().dismiss()
# Down_button1 = browser.find_element_by_id("aswift_1")
# Down_button1.click()


time.sleep(10)
browser.quit()
