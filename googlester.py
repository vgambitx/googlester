﻿from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time, os

driver = webdriver.Firefox('.')
driver.set_window_size(1024, 1024)
url = "https://google.com.ua"
delay = 2
element_name= 'q'
variants = (u'киеве', u'харькове', u'одессе', u'днепропетровске', u'донецке', u'запорожье', u'львове', u'кривом роге', u'николаеве', u'мариуполе', u'луганске', u'виннице', u'макеевке', u'севастополе', u'симферополе', u'херсоне', u'полтаве', u'чернигове', u'черкассах', u'житомире', u'сумах', u'хмельницке', u'черновцах', u'горловке', u'ровно', u'днепродзержинске', u'кировограде', u'ивано-франковске', u'кременчуге', u'тернополе', u'луцке', u'белой церкви', u'краматорске', u'мелитополе', u'керчи', u'никополе', u'ужгороде', u'славянске', u'бердянске', u'алчевске', u'павлограде', u'северодонецке', u'евпатории', u'лисичанске', u'каменец-подольске', u'броварах')
driver.get(url)
WebDriverWait(driver, delay).until(lambda driver : driver.find_element_by_name(element_name))
element = driver.find_element_by_name(element_name)
basename = os.path.basename(url)
if not os.path.isdir(basename):
    os.mkdir(basename)
for variant in variants:
    element.clear();
    query = u'в %s ' % variant
    element.send_keys(query)
    time.sleep(delay)
    driver.get_screenshot_as_file(basename + '/' + variant + '.png')
