Здравствуйте.
В 3-ем задании не удается никак реализовать добавление " путем list.insert(pos - 1, '"')
Если программа выглядит следующим образом программа не выполняется. Можете подсказать как было бы правильно добавить "кавычки" перед элементом списка.

my_text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
pos = 0
while pos < len(my_text):
    if my_text[pos].isdigit():
        my_text.insert(pos - 1, '"')
	my_text[pos] = my_text[pos].zfill(2)
        my_text.insert(pos + 1, '"')
    elif my_text[pos][1:].isdigit():
        my_text.insert(pos - 1, '"')
	my_text[pos] = my_text[pos].zfill(3)
        my_text.insert(pos + 1, '"')
    pos += 1

print(*my_text)