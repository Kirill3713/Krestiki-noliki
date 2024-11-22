# Импортируем модуль
import colorama
import os
# Объявляем переменные цветов
colorama.init()
green = colorama.Fore.GREEN
red = colorama.Fore.RED
blue = colorama.Fore.BLUE
cyan = colorama.Fore.CYAN
light_yellow = colorama.Fore.LIGHTYELLOW_EX
light_blue = colorama.Fore.LIGHTBLUE_EX
light_cyan = colorama.Fore.LIGHTCYAN_EX
black = colorama.Fore.BLACK
light_white = colorama.Fore.LIGHTWHITE_EX
light_magenta = colorama.Fore.LIGHTMAGENTA_EX
light_green = colorama.Fore.LIGHTGREEN_EX
light_red = colorama.Fore.LIGHTRED_EX
reset = colorama.Fore.RESET
# Определяем функцию
def start_game() -> None:
    """
    Игра "Крестики-нолики".
    """
    # Очищаем экран
    os.system("cls")
    # Поле для игры
    board = list(range(1, 10))
    # Счетчик ходов
    counter = 0
    # Устанавливаем флажок выигрыша
    is_win = False
    # Условия (координаты) победы
    win_coords = (
        (1, 2, 3), (4, 5, 6), (7, 8, 9),
        (3, 6, 9), (2, 5, 8), (1, 4, 7),
        (1, 5, 9), (3, 5, 7)
    )
    # Игроки
    tokens_list = [cyan + "✕" + reset, light_green + "⭘" + reset]
    # Напишем функцию для вывода игрового поля
    # Объявление функции
    def draw_board() -> None:
        """
        Функция отрисовки поля.
        """
        # Очищаем экран
        os.system("cls")
        print(green + "Игра Крестики - нолики" + reset)
        # Выводим поле
        for i in range(3):
            print(light_white + "-" * 13)
            print(light_white + "| " + light_blue + f"{board[0+i*3]}" + light_white + " | " + light_blue + f"{board[1+i*3]}" + light_white + " | " + light_blue + f"{board[2+i*3]}" + light_white +  " | ")    
        print(light_white + "-" * 13)
    # Запускаем основной цикл
    while not is_win:    
        # Вызываем функцию
        draw_board()
        # Меняем координаты на Х или О
        if counter % 2 == 0:
            player_token = tokens_list[0]
        else:
            player_token = tokens_list[1]
        coord_of_move = input(light_cyan + f"Куда поставить {player_token} ? " + light_magenta)
        # Проверка ввода
        if not coord_of_move.isdigit():
            input(light_red + "Некорректный ввод! Можно вводить только натуральные числа арабскими цифрами!" + red)
            continue
        coord_of_move = int(coord_of_move)- 1
        if coord_of_move > 8 or coord_of_move < 0:
            print(light_red + "Некорректный ввод! Введите номер свободного поля!")
            input(cyan + "(натуральное число в пределах девяти)" + red)
            continue
        # Это поле занято!
        if str(board[coord_of_move]) in tokens_list:
            print(light_red + "Это поле занято! Попробуйте еще раз.")
            input(black + "Нажмите Enter." + reset)
            continue
        else:
            board[coord_of_move] = player_token
            counter += 1
            # Проверка на победу и ничью
            if counter > 4:
                for win_coord in win_coords:
                    if board[win_coord[0]-1] == board[win_coord[1]-1] == board[win_coord[2]-1]:
                        is_win = True
                        os.system("cls")
                        draw_board()
                        print(light_yellow + f"{player_token} победили!")
                        quit()
            if counter == 9:
                os.system("cls")
                draw_board()
                print(light_yellow + "Ничья! Победила дружба!")
                quit()
        os.system("cls")
# Точка входа
if __name__ == "__main__":
    start_game()