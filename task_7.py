human = dict.fromkeys(['age', 'prof'])
for i in human.keys():
    if i == 'age':
        human['age'] = 32
    elif i == 'prof':
        human['prof'] = 'autotester'
print(human)