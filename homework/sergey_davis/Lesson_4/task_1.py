my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['apple', 'orange', 'banana', 'grape', 'kiwi'],
    'dict': {
        'name': 'Sergey',
        'age': 36,
        'city': 'Ulyanovsk',
        'course': 'Python',
        'level': 'beginner'
    },
    'set': {10, 20, 30, 40, 50}
}

print(my_dict['tuple'][-1])

my_dict['list'].append('avocado')
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = 'some value'
my_dict['dict'].pop('age')

my_dict['set'].add(60)
my_dict['set'].remove(20)

print(my_dict)
