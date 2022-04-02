my_text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_new_text = []
for element in my_text:
    if element.isdigit():
        my_new_text.append('"')
        my_new_text.append(element.zfill(2))
        my_new_text.append('"')
    elif element[1:].isdigit():
        my_new_text.append('"')
        my_new_text.append(element[:1] + element[1:].zfill(2))
        my_new_text.append('"')
    else:
        my_new_text.append(element)
print(*my_new_text)
