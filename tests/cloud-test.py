from Local import Local
from Cloud import Cloud
from tinydb import Query

cloud = Cloud('mongodb://test:password123@localhost:6000/trading?authSource=admin', 'trading')
local = Local('tests/res.json')


data1 = {
    'stock': 'SSI',
    'year': '2023',
    'algo': 'algo1',
    'pnl': '+2'
}

data2 = {
    'stock': 'BID',
    'year': '2022',
    'algo': 'algo1',
    'pnl': '+10'
}

data3 = {
    'stock': 'SSI',
    'year': '2020',
    'algo': 'algo2',
    'pnl': '100'
}
# cloud.delete('backtest', {'stock' : 'BID',  'year' : '2022'})

cloud.update('backtest', {'stock': 'SSI'}, {'pnl': '-100'})


cursor = cloud.db['backtest'].find()

# Iterate over the cursor to access each document
for document in cursor:
    print(document)