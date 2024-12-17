import re
import csv

#Задание 1:
with open('task1-ru.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()
capitalized_words = re.findall(r'\b[A-ZА-ЯЁ][a-zа-яё]+', text1)
words_before_colon = re.findall(r'\b[а-яА-ЯёЁa-zA-Z]+(?=:)\b', text1)
print("Задание 1:")
print("Слова с большой буквы:", capitalized_words)
print("Слова перед двоеточием:", words_before_colon)


#Задание 2:
with open('task2.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
closing_tags = set(re.findall(r'</(\w+)>', html_content))
print("\nЗадание 2:")
print("Закрывающие теги:", closing_tags)


#Задание 3:
with open('task3.txt', 'r', encoding='utf-8') as file:
    table_content = file.read()

ids = re.findall(r'(?<!\d-)\b[1-9]\d*\b(?!-\d)', table_content)
surnames = re.findall(r'\b[A-ZА-ЯЁ][a-zа-яё]+\b', table_content)
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.[a-z]{2,}\b', table_content)
registration_dates = re.findall(r'\b\d{4}-\d{2}-\d{2}', table_content)
websites = re.findall(r'\bhttps?://[\w.-]+\.[a-z]{2,}\b', table_content)

with open('task3_output.csv', "w", newline='', encoding='UTF-8') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=";")
    csv_writer.writerow(["ID", "Sirname", "Email", "Registration date", "Website"])
    for row in zip(ids, surnames, emails, registration_dates, websites):
        csv_writer.writerow(row)
print("\nЗадание 3:")
print("Данные по 3 заданию сохранены в output_task3.csv")


#Дополнительное задание:
with open('task_add.txt', 'r', encoding='UTF-8') as file:
    random_data = file.read()

# Ищем 5 дат, 5 email и 5 сайтов
found_dates = re.findall(r'(?<=\s)\d{2}[./-]\d{2}[./-]\d{4}|\d{4}[./-]\d{2}[./-]\d{2}', random_data)
found_emails = re.findall(r'(?<=\s)[\w.-]+@[\w.-]+\.[a-z]{2,}', random_data)
found_websites = re.findall(r'(?<=\s)https?://[\w.-]+\.[a-z]{2,}', random_data)

print("\nДополнительное задание:")
print("Найденные даты:", found_dates[:5])
print("Найденные email:", found_emails[:5])
print("Найденные сайты:", found_websites[:5])
