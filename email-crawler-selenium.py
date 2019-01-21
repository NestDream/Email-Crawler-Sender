#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   email-crawler-selenium.py
@Time    :   2019/01/21 23:30:57
@Author  :   Li Guo 
@Version :   1.0
@Contact :  gl_1997@outlook.com
@License :   Copyright (c) 2019 Li Guo
@Desc    :   None
'''

# Imported libs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


if __name__ == "__main__":
	with open("mail.txt","w+",encoding='utf-8') as file:
		emails = []
		url = ("http://cs.nankai.edu.cn/index.php/zh/2017-01-15-22-19-36/2017-01-15-22-20-52") # change the url to the website you want to crawl
		argument = ('lang=zh_CN.UTF-8')
		try:
			options = webdriver.ChromeOptions()
			options.add_argument(argument)
			driver = webdriver.Chrome(chrome_options=options)
			driver.get(url)
			time.sleep(3)
			elements = driver.find_elements_by_class_name("cloaked_email")
			if not elements:
				raise Exception(f"Cannot find element by class: {{cloaked_email}}")
			for element in elements:
				emails.append(element.get_attribute("textContent"))
			time.sleep(3)
			driver.execute_script("var q=document.documentElement.scrollTop=100000")
			driver.find_element_by_xpath('//*[@id="techerinformationList"]/tfoot/tr/td/div/ul/li[5]/a').click()
			driver.refresh()
			time.sleep(3)
			elements = driver.find_elements_by_class_name("cloaked_email")
			for element in elements:
				emails.append(element.get_attribute("textContent"))

		except Exception as identifier:
			print(identifier)
		finally:
			driver.quit()

		if emails:
			for email in emails:
				file.write(email+'\n')
