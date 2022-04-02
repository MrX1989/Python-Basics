my_text = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for element in my_text:
    element = str(element.title())
    text = element.split(' ')
    name = str(text.pop())
    print(f'Привет, {name}!')
