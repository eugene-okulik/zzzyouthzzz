secret_number = 7

while True:
    user_input = int(input('Угадайте число: '))
    if user_input == secret_number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("попробуйте снова.")
