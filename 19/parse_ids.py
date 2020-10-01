from ast import literal_eval
import json

ids = json.loads(open("ids").read().replace("'", '"'))

ids = list(map(lambda id : int(id.split('d')[0][1:-1]), ids))
ids.sort()

for id in ids:
    # id = id.split('d')[0][1:-1]
    print(id)
