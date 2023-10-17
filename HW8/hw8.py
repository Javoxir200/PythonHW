phone_book = []
fields = ["Фамилия", "Имя", "Телефон", "Описание"]


def show_menu():
    # print('\033c', end='') # Очистка экрана
    print(
        "1. Распечатать справочник",
        "2. Найти телефон в справочнике",
        "3. Изменить запись",
        "4. Удалить запись",
        "5. Добавить абонента в справочник",
        "6. Закончить работу",
        "",
        sep="\n",
    )


def show_menu_search():
    print("1. По фамилии", "2. По имени", "3. По номеру", "", sep="\n")


def show_ask_menu():
    print("Внести изменения?", "1. Да", "2. Нет", "", sep="\n")


def show_menu_rename():
    print("1. Фамилия", "2. Имя", "3. Телефон", "", sep="\n")


def work_with_phonebook():
    phone_book = read_txt("phonebook.txt")
    while 1:
        show_menu()
        match input():
            case "1":
                print_all_book()
            case "2":
                search_num()
            case "3":
                ask_rename()
            case "4":
                delete_line()
            case "5":
                add_new_line()
            case "6":
                break


# 1 Вывода на экран
def print_all_book():
    print(" ".join(k for k in phone_book[0].keys()))
    for line in phone_book:
        print_one_line(line)


def print_one_line(line):
    if line == 0:
        print("Не найдено!")
    else:
        print(" ".join(v for _, v in line.items()))


# Поиск
def search_num():
    field = ""
    search_str = ""

    show_menu_search()
    match input():
        case "1":
            field = "Фамилия"
        case "2":
            field = "Имя"
        case "3":
            field = "Телефон"
        case _:
            field = "Фамилия"

    line = try_to_find(phone_book, field)
    if line >= 0:
        print_one_line(phone_book[line])
        ask_rename(line)


def try_to_find(phone_book, field):
    str_f = input(f"Введите {field}: ")
    for line in range(len(phone_book)):
        if phone_book[line][field] == str_f:
            return line
    return -1


# Замена данных
def ask_rename():
    ask_one_rename(input("Введите номер записи которую хотите изменить: "))


def ask_one_rename(line):
    print_one_line(phone_book[int(line)])
    show_ask_menu()
    match input():
        case "1":
            rename_data(line)
        case "2":
            return


def rename_data(line):
    print("Что будем менять?")
    show_menu_rename()
    field = ""

    match input():
        case "1":
            field = "Фамилия"
        case "2":
            field = "Имя"
        case "3":
            field = "Телефон"

    phone_book[int(line)][field] = input(f"Введите {field}: ")
    write_txt("phonebook.txt", phone_book)


# БЛОК 4 Удалить запись
def delete_line():
    delete_one_line(input("Какую запись будем удалять?: "))


def delete_one_line(line):
    print_one_line(phone_book[int(line)])
    show_ask_menu()
    match input():
        case "1":
            phone_book.pop(int(line))
        case "2":
            return
    write_txt("phonebook.txt", phone_book)


# Добавление данных
def add_new_line():
    data = list()
    data.append(input("Введите Фамилию: "))
    data.append(input("Введите Имя: "))
    data.append(input("Введите Телефон: "))
    data.append(input("Введите Информацию: "))
    phone_book.append(dict(zip(fields, data)))
    write_txt("phonebook.txt", phone_book)


# Работы с файлом
def read_txt(filename):
    with open(filename, "r", encoding="utf-8") as phb:
        for line in phb:
            phone_book.append(dict(zip(fields, line.split(", "))))
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, "w", encoding="utf-8") as phout:
        for i in range(len(phone_book)):
            s = ""
            for v in phone_book[i].values():
                s += v + ","
            phout.write(f"{s[:-1]}\n")


work_with_phonebook()
