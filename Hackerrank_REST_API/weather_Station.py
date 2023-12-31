#Weather Station
def getnum(str):
  val = ''
  for c in str:
    if c.isdigit():
      val+=c
    else:
      if val !='':
        break

  return int(val)

def weatherStation(keyword):
  baseurl = ' https://jsonmock.hackerrank.com/api/weather/search'+ f'?name={keyword}'

  totalpages = 1
  pageno =1
  mylist = []
  while pageno <= totalpages:
    r = requests.get(baseurl +f'&page={pageno}')
    data = r.json()
    totalpages = data['total_pages']
    pageno+=1

    for obj in data['data']:
      currlist = []
      currlist.append(obj['name'])
      currlist.append(getnum(obj['weather']))
      currlist.append(getnum(obj['status'][0]))
      currlist.append(getnum(obj['status'][1]))
      mylist.append(currlist)

  mylist.sort(key = lambda x :x[0])

  return mylist

weatherStation('all')
