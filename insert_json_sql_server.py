# Reading / Inserting JSON Data
import pyodbc
import json

connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=mis5400-spring2019.database.windows.net,1433;Database=MIS5400;Uid=mckelly;Pwd=Mi$5400spring2019;'
conn = pyodbc.connect(connection_string,autocommit=True) # autocommit = True, since it is the SQL Server way

curs = conn.cursor()

# curs.execute(
#     '''
#     create table MKP_TIL_JSON(
#     ID int primary key clustered identity(1,1)
#     ,Title varchar(1000)
#     ,Domain varchar(1000)
#     )
#
#     '''
#     )


insert_query = 'insert into MKP_TIL_JSON (Title, Domain) values (?,?)'
with open(r'/tmp/data/todayilearned.json') as data_file:
    data = json.load(data_file)
    data_list = data['data']['children']
    rows_to_insert = []
    for entry in data_list:
        rows_to_insert.append(tuple([entry['data']['title'], entry['data']['domain']]))
    curs.executemany(insert_query, rows_to_insert)




# Commit and close the connection
conn.commit()
conn.close()
