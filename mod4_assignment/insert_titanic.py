'''This file will contain the functionality aspects
of my code that will create a cursor and connect
to my elephantSQL database and execute queries to or
on that database as well. My password and important
info from elephantSQL are kept safe because they are
not written here but in an env file that is imported
to a gitignore file. the gitignoe software is enabled
when i import getenv from os in this file.

We want to set up a new table for the Titanic data
(titanic.csv) - spend some time thinking about the
schema to make sure it is appropriate for the columns.
Enumerated types may be useful. Once it is set up,
write a insert_titanic.py script that uses psycopg2
to connect to and upload the data from the csv.
Then add the file to your repo. Fianlly, start
writing PostgreSQL queries to explore the data!'''

import pandas as pd
import psycopg2
from os import getenv


#accessing my secret info from my .env file
# must restart terminal to run the code for
# this to work after the modules are set up
DBNAME= 'otezlqst'
USER= 'otezlqst'
PASSWORD= '5rYIF4oXgvfCNbEzKpevCKvV9Wmu0UVh'
HOST= 'mahmud.db.elephantsql.com'


# make postgres connection and cursor enabling
    # our access to the postgres database through
    # elephantSQL
pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
pg_curs = pg_conn.cursor()


def execute_query_pg(curs, conn, query):
    '''execute query function does not need
    .fetchall in postgreSQL but we need a commit'''
    results = curs.execute(query)
    conn.commit()
    return results


#titanic table schema we are creating
TITANIC_TABLE = '''
CREATE TABLE IF NOT EXISTS titanic_table(
    passenger_id SERIAL PRIMARY KEY,
    Survived INT NOT NULL,
    Pclass INT NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Sex VARCHAR(10) NOT NULL,
    Age FLOAT NOT NULL,
    Siblings_Spouses_Aboard INT NOT NULL,
    Parents_Children_Aboard INT NOT NULL,
    Fare FLOAT NOT NULL
    );
    '''

DROP_TITANIC_TABLE = '''
    DROP TABLE IF EXISTS titanic_table;
'''

#read in our dataset from a csv file
df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].str.replace("'", " ")



if __name__ == '__main__':

    #create table and its associated scheme
    #drop table
    execute_query_pg(pg_curs, pg_conn, DROP_TITANIC_TABLE)
    #create table
    execute_query_pg(pg_curs, pg_conn, TITANIC_TABLE)
    #we now want to loop over our dataframe and insert
    # it inside of our database

#the dataframe must first be turned into a numpy array
# for the .tolist method to work
    records = df.values.tolist()

#if we print(records)
#we first get a list of lists when we print records
# but we want a list of tuples. this issue can be
# resolved when we loop over the records

    for record in records:
        insert_statement = f'''
            INSERT INTO titanic_table(Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
            VALUES {tuple(record)};
        '''
        execute_query_pg(pg_curs, pg_conn, insert_statement)
