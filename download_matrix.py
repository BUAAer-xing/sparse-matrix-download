import requests
import csv
from tqdm import tqdm

all_lists = {}
with open(file='all_matrix_information.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        all_lists[row[0]] = row[1]

with_limitation_lists = []
with open(file='with_limitation_matrix_information.csv',mode='r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        with_limitation_lists.append(row[1])

for filename in tqdm(with_limitation_lists[0:2]):
    if all_lists[filename]:
        link = all_lists[filename]
        response = requests.get(link)
        # 你可能需要从URL中提取文件名
        file_name = 'downloaded_matrixs/'+link.split('/')[-1]
        # 保存文件
        with open(file_name, 'wb') as file:
            file.write(response.content)

