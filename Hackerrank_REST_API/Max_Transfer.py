
#max transfer
import requests

pname = 'Bob Martin'
cityname = 'Bourg'

link = 'https://jsonmock.hackerrank.com/api/transactions'
credimax = 0
debitmax = 0

creditans = ""
debitans = ""
totalpages = 1
pageno =1
while pageno <= totalpages:
  res = requests.get(link + f'?page={pageno}')
  data = res.json()
  totalpages = data['total_pages']
  pageno+=1
  for obj in data['data']:
    if obj['userName'] ==pname and obj['location']['city'] ==cityname:
      val =float(obj['amount'][1:].replace(',' ,''))

      if obj['txnType'] == 'credit':
        if val > credimax:
          credimax = val
          creditans = obj['amount']

      elif obj['txnType'] == 'debit':
        if val > debitmax:
          debitmax = val
          debitans = obj['amount']



print([creditans,debitans])
