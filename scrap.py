import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):
    for month in range(1, 13):
        url = f'https://localhost/wp-content/uploads/{year}/{month:02d}/'
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a'):
            if link.get('href')[-4:].lower() == '.pdf':
                file = link.get('href')
                file_url = url + file
                response = requests.get(file_url)
                with open(f'downloads/{file}', 'wb') as f:
                    f.write(response.content)
