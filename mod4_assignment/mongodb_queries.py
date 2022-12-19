'''connect to rpg database client and then specific
collection using pymongo and use a class called mongoanswers
that executes a bunch of queries to answer a variety
of questions.'''

import pymongo
from queries import MongoAnswers

PASSWORD = '1TKUHyWgpIxF0J0g'
DBNAME = 'rpg_data'


client = pymongo.MongoClient(f'mongodb+srv://charlieblk9400:{PASSWORD}@cluster0.tszlrua.mongodb.net/{DBNAME}?retryWrites=true&w=majority')
#database
db = client.rpg_data
#collection
col = db['rpg_data']

#instantiate our class with our characters attribute and query methods
mongo_answers = MongoAnswers(col)


if __name__ == '__main__':
    print(mongo_answers.show_results())
