########################
# Microsoft SQL Server #
########################
'''
Options for hosting:
1) Local - Fastest, more control, can do bulk inserts for massive sets of data. Requires installation
2) Shared / On-Premise - "Stairway" server hosted by MIS. Must be connected to VPN
3) Cloud (e.g. Azure) - Good skill-set to have on resume. Available anywhere. Some instances are not fully-featured yet


There are many competing options for connecting to SQL Server.
https://wiki.python.org/moin/ODBC


ODBC Variants:
1) PYODBC (https://github.com/mkleehammer/pyodbc/wiki/) - Most Popular, great documentation.
2) PYPYODBC (https://github.com/jiangwen365/pypyodbc/)

Others:
3) PYMSSQL (https://github.com/pymssql/pymssql) - Good community support.
                                                - Documentation at http://pymssql.org/en/stable/
4) CTDS (https://github.com/zillow/ctds) - Used / maintained by Zillow, new.
                                                - Documentation at https://zillow.github.io/ctds/


Installing SQL Server ODBC Drivers:
Newest (ODBC 17): https://www.microsoft.com/en-us/download/details.aspx?id=56567
'''
import pyodbc


# Setup the Connection String - See
# https://www.connectionstrings.com/sql-server-native-client-11-0-odbc-driver/
#Driver={ODBC Driver 13 for SQL Server};Server=tcp:mis5400-spring2019.database.windows.net,1433;Database=MIS5400;Uid=mckelly;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=mis5400-spring2019.database.windows.net,1433;Database=MIS5400;Uid=mckelly;Pwd=Mi$5400spring2019;'

# Use .connect (DB API 2.0) to get a Connection Object
conn = pyodbc.connect(connection_string,autocommit=True) # autocommit = True, since it is the SQL Server way

# Create the cursor object
curs = conn.cursor()


# Use the execute method to execute SQL Statements
# Create the table (CPI For All Urban Consumers) / Note the SQL Server specific syntax
# curs.execute(
#     '''
#     create table CPI_MKP_Spring_2019(
#     ID int primary key clustered identity(1,1)
#     ,ObservationDate datetime
#     ,CPIAUCSL float
#     )
#
#     '''
#     )


# Insert some cpi data (R.B.A.R) !
# We are using the .executemany DB API V2.0 Method
import csv
insert_query = 'insert into CPI_MKP_Spring_2019 (ObservationDate, CPIAUCSL) values (?,?)'
with open(r'/tmp/data/fred_cpi.csv', 'r',encoding='utf8') as cpi_file:
    cpi = csv.reader(cpi_file)
    curs.executemany(insert_query, cpi)



# Commit and close the connection
conn.commit()
conn.close()


# Now open and read it using the .cursor object
conn =  pyodbc.connect(connection_string,autocommit=True)
curs = conn.cursor()

# First, execute the select query
query = 'select * from mis5400.dbo.CPI_MKP_Spring_2019'
curs.execute(query)

# Second, loop through each result using .fetchall()
# Note that the datatype is datetime.datetime, which we know how to use in Python
for row in curs.fetchall():
    print(row)

#Open to a local server to do bulk import
conn.close()
del conn

connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=localhost\SQL2017;Database=MIS5400;Trusted_Connection=yes;'
conn =  pyodbc.connect(connection_string,autocommit=True)
curs = conn.cursor()

# For processing bulk data, we can use a staging table
curs.execute(
    '''
    create table CPI_MKP_Spring_2019_Staging(
    ObservationDate datetime
    ,CPIAUCSL float
    )

    '''
    )

bulk_insert_sql = """
    bulk insert mis5400.dbo.CPI_MKP_Spring_2019_Staging
    from 'd:/data/fred_cpi.csv' with (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR='\n'
    );
"""

curs.execute(bulk_insert_sql)
conn.commit()
curs.close()
conn.close()


