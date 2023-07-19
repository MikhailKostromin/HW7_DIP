""" Напишите функцию группового переименования файлов.
Она должна:
1. принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
2. принимать параметр количество цифр в порядковом номере.
3. принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
4. принимать параметр расширение конечного файла.
5. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.
2.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами."""

import os
from os import listdir
from os.path import isfile, join


def rename_files(name, num_dig, extension, final_extension, from_name=0, to_name=0):
    count = 1
    only_files = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
    print(only_files)

    for file in only_files:
        if file.split('.')[-1] == extension:
            name_part = file.split('.')[0][from_name:to_name]
            if len(str(count)) != num_dig:
                tmp = (num_dig - len(str(count))) * '0'
                file_count = f'{tmp}{count}'
                print(file_count)
            file_name = f'{name_part}{name}{file_count}{final_extension}'
            print(file)
            os.rename(file, file_name)
            print(file_name)
            count += 1


if __name__ == '__main__':
    rename_files('Polina', 5, 'jpg', 'txt', 0, 0)
