from  import
from ..src import Cloud
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



query2 = Query().stock == 'SSI'
new_data = {'pnl': '-99'}  # New data to update

local.update('backtest', query2, new_data)




