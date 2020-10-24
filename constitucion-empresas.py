import os
from datetime import timedelta
import datetime
from bs4 import BeautifulSoup
import requests

def get_items_by_date(date: datetime.date):
    print('fetching %s' % date.strftime('%d-%m-%Y'))
    params = {
        'date': date.strftime('%d-%m-%Y')
    }

    url = 'https://www.diariooficial.interior.gob.cl/edicionelectronica/empresas_cooperativas.php'

    # Se hacen dos requests porque el primero redirige al index con numero edicion
    page = requests.get(url, params=params)
    page = requests.get(
        page.url.replace('index.php', 'empresas_cooperativas.php'),
        params=params)

    soup = BeautifulSoup(page.text, 'lxml')
    return soup.find_all('a', {'target': '_blank'})


def save_item_by_url(url: str, path: str):
    # Si ya se descargo el pdf, seguir con otro
    if os.path.exists('%s/%s' % (path, url.split('/')[-1])):
        print('.... SKIP %s' % url.split('/')[-1])
        return False

    print('.... SAVE %s' % url.split('/')[-1])

    pdf = requests.get(url)
    with open('%s/%s' % (path, url.split('/')[-1]), 'wb') as f:
        f.write(pdf.content)
    return True


def save_multiple_items_by_url(urls: list, path: str):
    for url in urls:
        save_item_by_url(url, path)
    return


def download_constituciones_by_date(date: datetime.date, path: str, filter='CVE-'):
    items = get_items_by_date(date)
    urls = []
    for item in items:
        if filter in str(item.next) and 'href' in item.attrs:
            pdf_url = item.attrs['href']
            urls.append(pdf_url)
    if urls:
        # Se crea el path si no existe
        if not os.path.exists(path):
            os.makedirs(path)

        for url in urls:
            save_item_by_url(url, path)
        return True
    return False


"""
path:string > path a la carpeta donde bajar los archivos
"""
def download_todays_constituciones():
    today = datetime.datetime.now().date()
    path = 'constituciones/%s' % today.strftime('%Y%m%d')
    return download_constituciones_by_date(today, path, filter='CVE-157')

"""
path:string > path a la carpeta donde bajar los archivos
year:number > año a descargar (ej: 2019)
"""


def download_constituciones_from_year(year: int):
    date = datetime.date(year, 1, 1)
    while date.year == year:
        path = 'constituciones/%s' % date.strftime('%Y%m%d')
        download_constituciones_by_date(date, path, filter='CVE-157')
        date += timedelta(days=1)


# num_days = 365
# for i in range(1, num_days + 1):

download_todays_constituciones()
download_constituciones_from_year(2019)
