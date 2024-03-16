import csv

with open('vacancy_new.csv',encoding='utf-8',newline=',') as file,open('newvacany_new',encoding='utf-8',newline=','):
    data = list(csv.reader(delimiter=';'))
