import progressbar
import csv
import os
import psycopg2

"""
Скрипт для миграции в базу данных, csv файло с данными из проектов Kaggle.
"""


def migrate_csv_file(file_path):
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')


"""Получаем список файлов"""

scandir = './data'

for dirname, dirnames, filenames in os.walk(scandir):
    for filename in filenames:
        filename_path = os.path.join(dirname, filename)
        filen, file_extension = os.path.splitext(filename_path)
        if file_extension != '.csv':
            continue
        print('Миграция файла: ' + filename)
        migrate_csv_file(filename_path)
