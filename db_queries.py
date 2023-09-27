
import sqlite3 as sql
conn = sql.connect('database.db')
def insert_table(table,row):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO {table} {tuple(row.keys())} VALUES ({','.join('?' for _ in range(len(row)))})",(tuple(row.values()) ))
            con.commit()
            msg = "Record successfully added"
            print(msg)
    except:
        con.rollback()
        msg = "error in insert operation"

    finally:
        con.close()


def get_columns(table):

    """have to look """
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            columns=cur.execute(f"select column_name from information_schema.columns where table_name = {table};")
            print(columns)
    except:
        print("error")
d={
'customer_id' : 101,
'name' : "harish",
'mobile' : 7013873682

}
insert_table('customer_details',d)

get_columns('customer_id')

