# Making and Reading from Dictionaires

x = {'age': '29', 'birthplace': 'Vietnam', 'favorite_language': 'Python', 'name': 'Hanh'}

print x['name']
print x['age']

def aboutYourself(x):
    for key,data in x.iteritems():
        print key, "=", str(data)
        
print aboutYourself(x)  

