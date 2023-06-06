from TinyDB import TinyDB
from MongoDB import MongoDB

cloud = MongoDB('mongodb://test:password123@localhost:6000/trading?authSource=admin', 'trading')
local = TinyDB('res')

data = {
    'algo': 'test',
    'result': '+10'
}
