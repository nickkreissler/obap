import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup

context = ssl._create_unverified_context()
response = urlopen("https://basketball.realgm.com/international/teams",context=context)
response = response.read().decode()
soup = BeautifulSoup(response, 'lxml')
x = soup.findAll('td')
a=0
c=0
b={}
for i in x:
    if a % 4!=0:
        b[c]+=[i.string]
        a+=1
    else:
        c+=1
        b[c]=[i.string]
        a+=1
c = {}
for i in b:
    c[i]=[]
    for j in b[i]:
        if j != None and j != '\xa0':
            c[i]+=[j]

d=[]
y = soup.findAll('a',href = True,text='Roster')
for link in y:
    d+=[link['href']]
f =0
for i in c:
    c[i]+=[d[f]]
    f+=1
print(c)
y = {}
for i in c:
    for j in c[i]:
        y[c[i][0]] = []

        response = urlopen("https://basketball.realgm.com/{}".format(c[i][len(c[i])-1]), context=context)
        print
        response = response.read().decode()
        soup = BeautifulSoup(response, 'lxml')
        for row in soup.findAll('table')[0].tbody.findAll('tr'):
            second_column = row.findAll('td')[1].contents
            for W in second_column:
                y[c[i][0]] += [W.string]

print(y)




t={}
for i in c:
    if c[i][len(c[i])-2] not in t.keys():
        t[c[i][len(c[i])-2]] = [c[i][0]]
    else:
        t[c[i][len(c[i])-2]] += [c[i][0]]
print(t)
q={}
for i in c:
    q[c[i][0]] = c[i][len(c[i])-2]

print(q)