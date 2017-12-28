import csv
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")

main_table = bsObj.findAll("table", {"class": "wikitable"})[0]  #findAll生成列表
rows = main_table.findAll("tr")

try:
    csvFile = open("../files/csvFile.csv", "wt", newline='', encoding='utf-8')
except FileNotFoundError:
    print(FileNotFoundError)
    os.mkdir("../files")
    csvFile = open("../files/csvFile.csv", "wt", newline='', encoding='utf-8')

writer = csv.writer(csvFile)


try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(["td", "th"]):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
# print(rows)