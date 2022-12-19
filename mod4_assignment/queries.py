'''All of my queries that directly answer the questions from the prompt'''

#query 0
TOTAL_SURVIVED = '''
    SELECT SUM(Survived) FROM titanic_table;
    '''
#query 1
TOTAL_DIED = '''
    SELECT count(*) FROM titanic_table
    WHERE survived = 0;
    '''
#query 2
TOTAL_EACH_CLASS = '''
    SELECT pclass, count(pclass)
    FROM titanic_table
    GROUP BY pclass;
    '''

#query 3
TOTAL_SURVIVED_EACH_CLASS = '''
    SELECT pclass, count(survived) FROM titanic_table
    WHERE survived = 1
    GROUP BY pclass;
    '''

#query 4
TOTAL_DIED_EACH_CLASS = '''
    SELECT pclass, count(survived) FROM titanic_table
    WHERE survived = 0
    GROUP BY pclass;
    '''

#query 5 
AVG_AGE_SURVIVED = '''
    SELECT AVG(age) FROM titanic_table
    WHERE survived = 1;
    '''

#query 6
AVG_AGE_DIED = '''
    SELECT AVG(age) FROM titanic_table
    WHERE survived = 0;
    '''
#query 7
AVG_AGE_EACH_CLASS = '''
    SELECT pclass, AVG(age) FROM titanic_table
    GROUP BY pclass;
    '''

#query 8
AVG_FARE_PER_CLASS = '''
    SELECT pclass, AVG(fare) FROM titanic_table
    GROUP BY pclass;
    '''


#query 9
AVG_FARE_PER_OUTCOME = '''
    SELECT survived, AVG(fare) FROM titanic_table
    GROUP BY survived;
    '''

#query 10
AVG_SIB_SPOUSE_PER_OUTCOME = '''
    SELECT survived, AVG(Siblings_Spouses_Aboard) 
    FROM titanic_table
    GROUP BY survived;
    '''

#query 11
AVG_SIB_SPOUSE_BY_CLASS = '''
    SELECT pclass, AVG(Siblings_Spouses_Aboard) 
    FROM titanic_table
    GROUP BY pclass;
    '''

#query 12
PARENTS_CHILDREN_PER_CLASS = '''
    SELECT pclass, AVG(Parents_Children_Aboard) 
    FROM titanic_table
    GROUP BY pclass;
    '''

#query 13
PARENTS_CHILDREN_PER_OUTCOME = '''
    SELECT survived, AVG(Parents_Children_Aboard) 
    FROM titanic_table
    GROUP BY survived;
    '''
#query 14
PASSENGERS_WITH_DIFF_NAMES = '''
    SELECT count(DISTINCT name)
    FROM titanic_table;
    '''







QUERY_LIST = [TOTAL_SURVIVED,
TOTAL_DIED,
TOTAL_EACH_CLASS,
TOTAL_SURVIVED_EACH_CLASS,
TOTAL_DIED_EACH_CLASS,
AVG_AGE_SURVIVED,
AVG_AGE_DIED,
AVG_AGE_EACH_CLASS,
AVG_FARE_PER_CLASS,
AVG_FARE_PER_OUTCOME,
AVG_SIB_SPOUSE_PER_OUTCOME,
AVG_SIB_SPOUSE_BY_CLASS,
PARENTS_CHILDREN_PER_CLASS,
PARENTS_CHILDREN_PER_OUTCOME,
PASSENGERS_WITH_DIFF_NAMES
]

#==============================================

#mongodb queries

class MongoAnswers():
    def __init__(self, col):
        #get all documents
        self.col = col
        self.characters = col.find({})

    def total_characters(self):
        return len(list(self.characters))

    def show_results(self):
        return(f'''
        Total Number of Characters: {self.total_characters()}
        ''')
