import shelve


db = shelve.open('personshelvedb')
for key in db:
    print(key, db[key], sep = ' => ')
man1 = db['Mechael Dodo']
print('Befor: ', man1)
man1.giveRaise(0.05)
print('After: ', man1)
db['Mechael Dodo'] = man1

db.close()


