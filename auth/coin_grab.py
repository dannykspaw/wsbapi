from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from config import creds

## grab crypto currency coins
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
parameters = {
  'start':'1',
  'limit':'2',
  'sort':'cmc_rank'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '{}'.format(creds['coingrabkey']),
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

data_payload = data['data']
print(data_payload[0])

symbol_lexicon = {}
symbol_data = []

# build lexicon of symbols
for x in data_payload:
    symbol_data.append(x['name'])
    symbol_data.append(x['symbol'])
    symbol_data.append(x['slug'])
    symbol_data.append(str('$' + x['symbol']))
    symbol_data.append(str(x['symbol']).lower())
    symbol_data.append(str('$' + x['symbol']).lower())

    symbol_lexicon[x['symbol']] = symbol_data

    symbol_data = []

print(symbol_lexicon)