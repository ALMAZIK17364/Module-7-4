import os
from os import *
import time

file_path = 'file.txt'
abs_path = os.path.abspath(file_path)
dir_path = os.path.dirname(abs_path)
directory = dir_path

print(dir_path)

for root, dirs, files in os.walk(directory):
    for file in files:
        file_full_path = os.path.join(root, file)
        filepath = os.path.abspath(file_full_path)
        filetime = os.path.getatime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, '
              f'Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')