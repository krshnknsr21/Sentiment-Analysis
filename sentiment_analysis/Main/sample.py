import pymysql

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="2001",
        db='Sample_1',
    )
    cur = conn.cursor()
    cur.execute("select * from persons")
    output = cur.fetchall()

    for i in output:
        print(i)

    # To close the connection
    conn.close()


# Driver Code
# if __name__ == "__main__":
#     mysqlconnect()
