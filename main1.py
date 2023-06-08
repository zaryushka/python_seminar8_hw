# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.

# создаем пустой список
# контакты будут в виде: фамилия, имя, номер. т.е. будет список списков
# phonebook = [['Петров', 'Петр', '222'], ['Иванов', 'Иван', '333']] и т.д.
phonebook = []
import csv

# показать все контакты
def print_result():
    if len(phonebook) == 0:
        print('Список контатков пуст')
    else:
        for contact in phonebook:
            print(contact)

# поиск контакта по фамилии
def search_name(last_name):
    result = []
    for contact in phonebook:
        if contact[0].lower() == last_name.lower():
            result.append(contact)
    if len(result) == 0:
        print('Контакт с фамилией', last_name.title(), 'не найден')
    else:
        print(*result)


# поиск контакта по номеру
def search_number(number):
    result = []
    for contact in phonebook:
        if number in str(contact[2]):
            result.append(contact)
    if len(result) == 0:
        print('Контакт с номером', number, 'не найден')
    else:
        print(*result)

# добавить контакт
def add_contact():
    last_name = input('Введите фамилию: ').title()
    name = input('Введите имя: ').title()
    number = input('Введите номер телефона: ')
    phonebook.append([last_name, name, number])
    print(*phonebook, sep='\n')


# удалить контакт
def del_contatct():
    last_name = input('Введите фамилию: ')
    for contact in phonebook:
        if contact[0].lower() == last_name.lower():
            phonebook.remove(contact)
            print('Контакт удален')
            return True
    print('Контакт не найден')
    return False
        

# сохранить справочник в файл
def save_file():
    file_name = input('Введите имя файла: ')
    with open(file_name, 'a', encoding='utf-8') as file:
        for contact in phonebook:
            file.write(contact[0] + ' ' + contact[1] + ' ' + contact[2] + '\n')


# загрузить справочник из файла
def load_file():
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            phonebook.append(row)
            print(row)


# основное меню, бесконечный цикл
while True:
    print('1. Показать все контакты')
    print('2. Поиск контакта по фамилии')
    print('3. Поиск контакта по номеру')
    print('4. Добавить контакт')
    print('5. Удалить контакт')
    print('6. Сохранить справочник в файл')
    print('7. Загрузить справочник из файла')
    print('8. Выход')
    choice = int(input('Выберите пункт меню: '))
    if choice == 1:
        print_result()
    elif choice == 2:
        search_name(input('Введите фамилию: '))
    elif choice == 3:
        search_number(input('Введите номер телефона: '))
    elif choice == 4:
        add_contact()
    elif choice == 5:
        del_contatct()
    elif choice == 6:
        save_file()
    elif choice == 7:
        load_file()
    elif choice == 8:
        break
    else:
        print('Некорректный ввод')