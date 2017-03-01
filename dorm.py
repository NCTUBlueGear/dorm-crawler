# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# Crawl the website
url = "http://dormapply2.adm.nctu.edu.tw/SecondResult/Second105.html"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml", from_encoding='big5')

# Get Familiar with the data

# print(soup.prettify())

# for row in soup.find_all('tr')[1:3]:
#     for idx, val in enumerate(row.find_all('td')):
#         print(idx, val.text)
#     print("--")

# Iterate through the rows and parse it
payloads = []
for row in soup.find_all('tr')[1:100]:
    room_no = ""
    for idx, val in enumerate(row.find_all('td')):
        if idx==1:
            room_no = val.text
        if idx==2:
            stu_list = val.text.split("\xa0\xa0\xa0")[:-1]
            for stu in stu_list:
                s = stu.split("(")
                if "(未確認申請)" in stu:
                    print(s[0], room_no , s[2][:-1])
                    payloads.append([s[0], room_no , s[2][:-1]])
                else:
                    print(s[0], room_no, "")
                    payloads.append([s[0], room_no , ""])

# Create csvfile
import csv
with open('output.csv', 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(payloads)