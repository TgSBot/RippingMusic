from os import listdir
from os.path import exists, isfile, join
from shutil import copy


def path_input():
    path = input('Введите путь вствки: ')
    while exists(path):
        print('Неправильный путь')
        path = input('Введите путь файла: ')
    return path


def path_output():
    path = input('Введите путь исходного: ')
    while exists(path):
        print('Неправильный путь')
        path = input('Введите путь файла: ')
    return path


if __name__ == '__main__':
    sending = path_input()
    path = path_output()

    count = 0
    for file in listdir(path):
        if isfile(join(sending, file)):
            pass
        else:
            copy(join(path, file), join(sending, file))
            count += 1
            print(f'Ваш файл {file} был перенеён в папку {sending}. {count}')
