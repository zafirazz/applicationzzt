from bs4 import BeautifulSoup
import requests
import os

#url = 'https://www.imdb.com/chart/top/'
def im_install(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'html.parser')
    os.chdir(os.path.join(os.getcwd(), folder))
    images = s.find_all('img')

    for im in images:
        name = im['alt']
        link = im['src']
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im1 = requests.get(link)
            f.write(im1.content)
            print(name)
im_install("https://www.companyfolders.com/blog/great-movie-poster-designs",'topmovies')








