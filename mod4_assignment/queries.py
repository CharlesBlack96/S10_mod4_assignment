'''All of my queries that directly answer the questions from the prompt. 
At the end of the day i do beleive noSQL if far more
diverse and applicable and complicated. SQL if
comfortable but i believe noSQL can be more diverse
hance more useful.'''

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
        self.characters = list(col.find({}))

    def total_characters(self):
        return len(self.characters)
    
    def total_items(self):
        count = 0
        for character in self.characters:
            count += len(character['items'])
        return count

    def total_weapons(self):
        count = 0
        for character in self.characters:
            count += len(character['weapons'])
        return count

    def total_non_weapons(self):
        return self.total_items() - self.total_weapons()

    def character_weapons(self):
        weapons_list = []
        for character in self.characters[:20]:
            num_weapons = len(character['weapons'])
            weapons_list.append((character['name'], num_weapons))
        return weapons_list

    def character_items(self):
        items_list = []
        for character in self.characters[:20]:
            num_items = len(character['items'])
            items_list.append((character['name'], num_items))
        return items_list

    def average_items(self):
        num_items = []
        for character in self.characters:
            num_items.append(len(character['items']))
        return (sum(num_items) / len(num_items))

    def average_weapons(self):
        num_weapons = []
        for character in self.characters:
            num_weapons.append(len(character['weapons']))
        return (sum(num_weapons) / len(num_weapons))


    def show_results(self):
        return(f'''
        Total Number of Characters: {self.total_characters()}
        Total Number of Items: {self.total_items()}
        Total Number of Weapons: {self.total_weapons()}
        Total Number of non-Weapons: {self.total_non_weapons()}
        Number of Weapons per Character (first 20): {self.character_weapons()}
        Number of items per Character (first 20): {self.character_items()}
        Average number of items per character: {self.average_items()}
        Average number of weapons per character: {self.average_weapons()}
        ''')


