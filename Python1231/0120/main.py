import mariadb
from dotenv import load_dotenv
load_dotenv()
import os

def getConn():
    try:
        return mariadb.connect(
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        port=int(os.getenv('PORT')),
        database=os.getenv('DATABASE')
        )  
    except mariadb.Error as e:
        print(f'MariaDB Error: {e}')
        return None     

def findOne(sql):
    result = None
    try:
        conn = getConn()
        if conn:
            cur = conn.cursor()
            cur.execute(sql) 
            row = cur.fetchone()
            columns = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()
            return dict(zip(columns, row))if row else None
    except mariadb.Error as e:
        print(f'MariaDB Error: {e}')
    return result


def findAll(sql):
    result = []
    try:
       conn = getConn()
       if conn:
            cur = conn.cursor()
            cur.execute(sql) 
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()
            result = [dict(zip(columns, row))for row in rows]
    except mariadb.Error as e:
        print(f'MariaDB Error: {e}')
    return result        

def save(sql):
    result = False
    try:
        conn = getConn()
        if conn:
            cur = conn.cursor()
            cur.execute(sql) 
            conn.commit()
            cur.close()
            conn.close()
            return True
    except mariadb.Error as e:
        print(f'MariaDB Error: {e}')
    return result

deftNo1 = 'd001'
deftNo2 = 'd002'
deftNo3 = 'd009'
defList = [deftNo1, deftNo2, deftNo3]

# 셀렉
selectSql = f'''
select * from edu.test
    '''

# 추가
name = '수아짱짱맨뿡뿡'
insertSql = f'''
INSERT INTO edu.test (`name`,`regdate`)
VALUE ('{name}', NOW())
'''

# 삭제
table = 'edu.test'
condition = '`no` = 5'
deleteSql =f'''
DELETE FROM {table} WHERE {condition};
'''
# 수정
condition = "`name` = '안녕', `regdate` = '2000-00-00'"
condition2 ='`no`=1'
updateSql =f'''
UPDATE edu.test SET {condition}
WHERE {condition2};
'''

# print(sql)

# print(findOne(selectSql))
print(findAll(selectSql))
# print(save(insertSql))
print(save(deleteSql))
# print(save(updateSql))

