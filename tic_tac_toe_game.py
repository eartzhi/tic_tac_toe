def desk_view():
    print(f'\n    |  0  |  1  |  2\n'
          f'----+-----+-----+-----\n'
          f' 0  |  {desk[0][0]}  |  {desk[0][1]}  |  {desk[0][2]}\n'
          f'----+-----+-----+-----\n'
          f' 1  |  {desk[1][0]}  |  {desk[1][1]}  |  {desk[1][2]}\n'
          f'----+-----+-----+-----\n'
          f' 2  |  {desk[2][0]}  |  {desk[2][1]}  |  {desk[2][2]}\n')


def straight_diagonal(my_array):
    count_x, count_o = 0, 0
    for i in range(3):
        if my_array[i][i] == 'X':
            count_x += 1
        elif my_array[i][i] == 'O':
            count_o += 1
    return count_x == 3 or count_o == 3


def reverse_diagonal(my_array):
    count_x, count_o = 0, 0
    for i in range(3):
        if my_array[i][2 - i] == 'X':
            count_x += 1
        elif my_array[i][2 - i] == 'O':
            count_o += 1
    return count_x == 3 or count_o == 3


def line(my_array):
    for i in my_array:
        if i == ['X', 'X', 'X'] or i == ['O', 'O', 'O']:
          return True


def column(my_array):
    for j in range(3):
        count_x, count_o = 0, 0
        for i in range(3):
            if my_array[i][j] == 'X':
                count_x += 1
            if my_array[i][j] == 'O':
                count_o += 1
        if count_x == 3 or count_o == 3:
            return True


def move(number):
    for i in range(5):
        wrong_input = False
        player_move = input(f'Игрок №{number} введите координаты (x y) '
                            f'выбранного поля через пробел  ').split(' ')
        if len(player_move) != 2:
            print(f'Вы должны ввести две координаты через пробел.' 
                  f'Осталось {4 - i} попыток\n')
            wrong_input = True
            continue
        if not all([player_move[0].isdigit(), player_move[1].isdigit()]):
            print(f'Координаты должны быть числом. Осталось {4 - i} попыток\n')
            wrong_input = True
            continue
        player_move = tuple(map(int, player_move))
        if not all([0 <= player_move[0] <= 2, 0 <= player_move[1] <= 2]):
            print(f'Координаты должны быть в пределах от 0 до 2.' 
                  f'Осталось {4 - i} попыток\n')
            wrong_input = True
            continue
        if player_move in moves:
            print(f'Клетка занята. Осталось {4 - i} попыток\n')
            wrong_input = True
            continue
        break
    return player_move, wrong_input


desk = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
moves = []

print('**********************')
print('Игра в крестики-нолики')
print('**********************\n')

desk_view()
win = False
while True:
    for n in range(1, 3):
        coordinates, input_error = move(n)
        if input_error:
            print('Закончились попытки ввода. Игра прервана')
            break
        moves.append(coordinates)
        if n == 1 and desk[coordinates[1]][coordinates[0]] == '-':    # меняем местами координаты,
            desk[coordinates[1]][coordinates[0]] = 'X'                # чтобы x был на первом месте
        elif n == 2 and desk[coordinates[1]][coordinates[0]] == '-':  # для X и O
            desk[coordinates[1]][coordinates[0]] = 'O'
        desk_view()
        win = any([line(desk), straight_diagonal(desk),
                   reverse_diagonal(desk), column(desk)])
        if win:
            print(f'****************\n'
                  f'Выиграл игрок №{n}\n'
                  f'****************\n')
            break
        if len(moves) == 9:
            print('*****\n'
                  'Ничья\n'
                  '*****')
            break
    if any([input_error, win, len(moves) == 9]):
        break