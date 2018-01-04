from urllib.request import urlopen
from io import StringIO
import csv

csvFile = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode("ascii", "ignore")
datafile = StringIO(csvFile) # 将csv文件存储到内存
csvReader = csv.reader(datafile) # 结果转换为列表
# for row in csvReader:
#     print(row)

csvDicReader = csv.DictReader(datafile)

print(csvDicReader.fieldnames)  #第一行存储在fieldnames
for row in csvDicReader: # 结果为字典
    print(row)