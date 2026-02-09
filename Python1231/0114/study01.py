#arr = [1,2,3,4,5]
#for i in range(1,4,2):
#    print(i)

# arr = [[1,2],["a"],["가","나","다"]]
# for i in (arr):
#     print (i)
#     print (type(i))
#     if len(i)>1: print(i[1])

arr2 = [1,2,3]
arr2 = dict() #형변환 함수 not class
print(arr2)
# 이때 dict는 무조건 key가 필요함 그냥 (arr2)하면 value만 있어서 오류남

# 방법1: enumerate(): (index, value)형태의 튜플 생성
arr2 = [1,2,3]
arr2_dict1 = dict(enumerate(arr2))
print(arr2_dict1)

# 방법2: key 직접 지정
arr2 = [1,2,3]
key =("a""b""c")
arr2_dict2 = dict(zip(key,arr2))
print(arr2_dict2)
'''
{}
{0: 1, 1: 2, 2: 3}
{'a': 1, 'b': 2, 'c': 3}
'''

obj={}
obj["key"]=10
# obj={key: 10}

arr=[1]  # 이때 []가 빈 값이면 오류남
arr[0] = 10 #얘가 js와 다르게 추가가 아니라 !!변경!!이라서
print(arr)
# 즉 추가하려면 함수가 필요

arr =[1,2,3,4]
arr.pop(1)
print(arr)


user = {
    "name": "수아",
    "age": 20,
    "city": "Seoul"
}

user2 = {
             "name": "바봉"
}
print(user2 | user)  # 뒤에 오는 값이 덮어씌워짐

#for문 시퀀스로 만드는 방법
list =[]
for a in range(5):
    list.append(a)
print(list)
