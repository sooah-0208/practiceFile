import json

def getData():
    f = open('./data/memo.json', 'r', encoding='utf-8')
    return json.load(f)

def add(a, b):
    data = getData()
    result = int(a) + int(b)
    data['list'].append(result)
    print(data, f"합: {result}")
    f= open('./data/memo.json', 'w', encoding='utf-8')
    json.dump(data, f, ensure_ascii=False)

def list():
    print('list() 호출됨')
    data = getData()
    arr = data["list"]
    # print(data["txt"])  # 값 가져올 때 JS data.txt => PY data["txt"]
    for v in arr: print(v)
