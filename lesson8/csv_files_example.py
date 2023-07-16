import csv


with open('birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)

with open('birthday.txt', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)

with open('birthday.csv', 'w') as birthday:
    birthday_writer = csv.writer(birthday, delimiter=',',quotechar="'",quoting=csv.QUOTE_MINIMAL)
    birthday_writer.writerow(['Markus','python',2])
    birthday_writer.writerow(['alejandro','c++',4])

with open('birthday2.csv', 'w') as birthday:
    birthday_fieldnames = ['name','group', 'birthday']
    birthday_dict_writer = csv.DictWriter(birthday, fieldnames=birthday_fieldnames)
    birthday_dict_writer.writeheader()
    birthday_dict_writer.writerow({'name':'Emmanuel', 'group':'french', 'birthday':'8'})
    birthday_dict_writer.writerow({'name':'Boris', 'group':'english',"birthday":'10'})
    birthday_dict_writer.writerows([{'name':'Emmanuel', 'group':'french', 'birthday':'8'},{'name':'Boris', 'group':'english',"birthday":'10'}])
