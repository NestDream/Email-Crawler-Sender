#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   email-crawler-bf4.py
@Time    :   2019/01/21 23:28:29
@Author  :   Li Guo 
@Version :   1.0
@Contact :  gl_1997@outlook.com
@License :   Copyright (c) 2019 Li Guo
@Desc    :   None
'''

# Imported libs
import requests
import re
from bs4 import BeautifulSoup

# change the url to the website you want to crawl
main_addr = 'http://ai.nankai.edu.cn'

with open("outputemail-ai.txt", 'w+', encoding='utf-8') as file:
    people = []
    for i in range(1, 5):
        page_to_crawl = "/contentDetail/teachingStaffInit.action?channelId=c_0402&flag=" + str(i)
        requests.adapters.DEFAULT_RETRIES = 10
        s = requests.session()
        s.keep_alive = False
        resp = s.get(main_addr + page_to_crawl)
        s.close()

        html_doc = str(resp.content.decode('utf-8'))

        soup = BeautifulSoup(html_doc, "html.parser")
        links = soup.find_all('a')

        for link in links:
            if 'href' in link.attrs and 'faculty' in link['href']:
                people.append(main_addr + link['href'])

    print(people)

    for i in range(len(people)):
        s2 = requests.session()
        s2.keep_alive = False  
        resp_temp = s2.get(people[i])
        s2.close()

        html_doc_temp = str(resp_temp.content.decode('utf-8'))
        soup = BeautifulSoup(html_doc_temp, "html.parser")
        lis = soup.find_all('span')

        name = ''
        email = ''
        for li in lis:
            info = (li.get_text())
            match = (re.search(r'[0-9a-zA-Z_]{0,19}@nankai.edu.cn', info)) # change the re for your need
            try:
                match.string
            except AttributeError:
                pass
            else:
                email = match.group(0).strip()
                file.write(email + '\n')
                print(email)
