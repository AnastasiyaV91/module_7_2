def custom_write(file_name, strings):

    strings_positions = {}                         # Открываем пустой словарь  strings_positions
    file = open(file_name, 'w', encoding='utf-8')  # Открываем файл file_name в режиме 'w' с кодировкой encoding='utf-8'
                                                   # Если файла нет,  то он создается
    for num_line, line in enumerate(strings, start=1):    # Получаем кортеж в виде (num_line, line)
        first_byte = file.tell()                          # Сохраняем номер байта начала строки
        file.write(line + '\n')                           # Записываем в файл строку с переносом \n
        strings_positions[(num_line, first_byte)] = line  # Записываем в словарь strings_positions значения, где
                                                          # (num_line, first_byte) - ключ
                                                          # line - значение
    return strings_positions                              # Возвращаем значение словаря strings_positions
    file.close()                                          # Закрываем файл (обязательно)


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)