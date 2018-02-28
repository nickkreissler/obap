import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup

context = ssl._create_unverified_context()
response = urlopen("https://basketball.realgm.com/international/stats/2018/Averages/Qualified/All/points/All/desc/"+str(i), context=context)
response = response.read().decode()
soup = BeautifulSoup(response, 'html.parser')