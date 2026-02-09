import json

def getData():
    f = open("./data/words.json", "r", encoding="utf-8")
    result = json.load(f)
    f.close()
    return result

def setData(data):
    f = open("./data/words.json", "w", encoding="utf-8")
    json.dump(data, f, ensure_ascii=False)
    f.close()
    목록(True)

def empty():
    print("목록이 없습니다.")


# 윤우
def 입력(args):
	data=getData()
	id = max((word["id"] for word in data["words"]), default = 0 ) + 1
	row = { "id" : id, "word" : args.t }
	data["words"].append(row)
	setData(data)

#수아

def 수정(args):
	data=getData()
	for i in range(len(data['words'])):
		if data['words'][i]['id'] == int(args.k):
			data['words'][i]['word'] = args.t
			break
	setData(data)

#영윤
def 삭제(args):
	data= getData()
	for i in range(len(data["words"])):
		if data["words"][i]["id"] == int(args.k):
			del data["words"][i]
			break
	setData(data)

def 목록(args):
	data = getData()
	row1 = "="*40
	row2 = "-" *40
	print(row1)
	print(f'ID\t단어')
	print(row2)
	for i in range(len(data["words"])):
		print(f'{data["words"][i]["id"]}\t{data["words"][i]['word']}')
		if len(data["words"]) == 0 : print('입력값x')

		if i+1<len(data["words"]) : print(row2)
	print(row1)