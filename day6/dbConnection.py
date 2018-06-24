import pymysql
class DBconnection:
    def execute_sql_command(self):
        conn=pymysql.Connect( host="127.0.0.1", user="root", password="root",
                 database="pirate", port=3306,charset='utf8')


        # conn=pymysql.Connect(host="127.0.0.1", user="root", password="root",
        #          database="pirate", port="3306", charset='utf8')
        # conn = pymysql.Connect(host='127.0.0.1', user='root', password="root",
        #                        database='pirate', port=3306, charset='utf8')
        try:
            cursor=conn.cursor()
            sql="select * from hd_user order by id desc;"
            cursor.execute(sql)
            row=cursor.fetchone()

            conn.commit()
            return row
        finally:
            conn.close()
if __name__=="__main__":
    DBconnection().execute_sql_command()

