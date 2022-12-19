'''Connection to our postgresql elephant database.
Connect to the titanic dataset and query to answer
a variety of question. For organization sake we then
loop through our list of queries and enumerate and
display them together in one list.'''


from os import getenv
import psycopg2
from queries import QUERY_LIST

#install psycopg2-binary
#accessing my secret info from my .env file
# must restart terminal to run the code for
# this to work after the modules are set up
#must install pipenv instal python-dotenv
# after code is written close down VE and terminal and restart them to enable code to work.

#my env connection is not working
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
    curs.execute(query)
    return curs.fetchall()

def execute_queries(curs, conn, queries):
    answers_dict = {}
    for index, query in enumerate(queries):
        answers_dict[index] = execute_query_pg(curs, conn, query)
    return answers_dict


if __name__ == '__main__':
    answers_dict = execute_queries(pg_curs, pg_conn, QUERY_LIST)
    for index, value in enumerate(answers_dict.values()):
        print(f'{index}: {value}')
