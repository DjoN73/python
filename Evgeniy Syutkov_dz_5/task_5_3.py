from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]


my_gen = ((tutors[i], klasses[i]) for i in range(len(tutors) - 1))

#print(*zip_longest(tutors, klasses))

print(type(my_gen))
for i in range(len(tutors) - 1):
    print(next(my_gen))

print(*my_gen())



