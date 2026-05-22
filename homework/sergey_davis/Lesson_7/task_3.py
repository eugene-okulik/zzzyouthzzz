def print_result(text):
    parts = text.split(':')
    number = int(parts[1].strip())
    print(number + 10)


result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'
result_4 = 'результат: 2'

print_result(result_1)
print_result(result_2)
print_result(result_3)
print_result(result_4)
