from os import listdir
from os.path import exists, isfile, join
from shutil import copy


def path():
    path = input('Введите путь ')
    while exists(path):
        print('Неправильный путь')
        path = input('Введите путь файла: ')
    return path


if __name__ == '__main__':
    sending = path()
    path = path()

    count = 0
    for file in listdir(path):
        if isfile(join(sending, file)):
            pass
        else:
            copy(join(path, file), join(sending, file))
            count += 1
            print(f'Ваш файл {file} был перенеён в папку {sending}. {count}')
