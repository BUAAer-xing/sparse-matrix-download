import requests
from bs4 import BeautifulSoup
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

for link in download_links_MM[0:1]:
    # 下载文件
    if link :
        response = requests.get(link)
        # 你可能需要从URL中提取文件名
        file_name = link.split('/')[-1]
        # 保存文件
        with open(file_name, 'wb') as file:
            file.write(response.content)