import sqlite3 as sql
import csv    # csv 파일

def connect_db(db_name):
    conn = sql.connect(db_name)
    c = conn.cursor()
    return conn, c

def close_db(conn):
    conn.close()

def execute_sql(conn, c, sql, params=()):
    c.execute(sql, params)
    conn.commit()

def select_sql(conn, c, sql, params=()):
    c.execute(sql, params)
    rows = c.fetchall()
    for row in rows:
        print(row)

def select_emp(conn, c, sql):
    c.execute(sql)
    rows = c.fetchall()
    return rows

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

########################################################################
# start
# 데이터베이스 연결
conn, c = connect_db('..\\DB\\YBDB.db')

"""
# 함수 사용 예시
#execute_sql(conn, c, "INSERT INTO emp VALUES (?, ?, ?)", (1, 'John Doe', 'Engineer'))
#select_sql(conn, c, "SELECT * FROM emp")

#execute_sql(conn, c, "DELETE FROM emp WHERE id = ?", (1,))
"""
execute_sql(conn, c, "update emp set emp_name = ? WHERE emp_no = ?", ('홍길동 Doe', 2))
select_sql(conn, c, "SELECT * FROM emp")

# emp 테이블에서 데이터 선택
data = select_emp(conn, c, "SELECT * FROM emp")

# 데이터를 CSV 파일로 저장
save_to_csv(data, 'emp_data.csv')

# 연결 종료
close_db(conn)

