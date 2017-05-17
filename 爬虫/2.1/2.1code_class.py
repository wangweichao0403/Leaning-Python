import pymongo

client=pymongo.MongoClient('localhost',27017)
walden = client['walden']
sheet1 = walden['sheet1']
path = 'D:\walden.txt'
with open(path,'r') as f:
    lines = f.readlines()
    for index,line in enumerate(lines):
        data = {
            'index':index,
            'line' :line,
            'words':len(line.split())
        }
        sheet1.insert_one(data)