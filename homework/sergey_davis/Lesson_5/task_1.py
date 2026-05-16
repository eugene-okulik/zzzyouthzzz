# Задание 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

print(name, last_name, city, phone, country)

# Задание 2

result_1 = 'результат операции: 32'
result_2 = 'результат операции: 504'
result_3 = 'результат работы программы: 9'

number_1 = int(result_1[result_1.index(':') + 2:])
print(number_1 + 10)

number_2 = int(result_2[result_2.index(':') + 2:])
print(number_2 + 10)

number_3 = int(result_3[result_3.index(':') + 2:])
print(number_3 + 10)

# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

students_text = ', '.join(students)
subjects_text = ', '.join(subjects)

print(f'Students {students_text} study these subjects: {subjects_text}')
