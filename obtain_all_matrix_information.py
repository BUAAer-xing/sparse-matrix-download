import requests
from bs4 import BeautifulSoup
import csv
# 网址
url = 'http://sparse.tamu.edu/?per_page=All'

# 发送请求获取网页内容
response = requests.get(url)
web_content = response.content

# 解析网页
soup = BeautifulSoup(web_content, 'html.parser')

download_links = soup.find_all(name='a', class_='btn btn-outline-dark btn-sm')
download_links_MM = []
file_name_and_url = {}

for link in download_links:
    if link.getText(strip=True) == 'Matrix Market':
        download_links_MM.append(link.attrs['href'])
        file_name_and_url[link.attrs['href'].split('/')[-1]] = link.attrs['href']

with open('all_matrix_information.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['File Name', 'Link'])
    for link in file_name_and_url:
        tmp = [link, file_name_and_url[link]]
        csv_writer.writerow(tmp)
