print('*'*50+ 'Калькулятор' + "*"*40)
true_action = ['*', "/", "+", "-"]
def calculate(x, y, action):
    if action == '-':
        z = x-y
    elif action == '+':
        z = x+y
    elif action == '*':
        z = x*y
    elif action == '/':
        z = x/y
    else:
        z = 'error'
    return z
while True:
    print(f'чо надо абобус') #Ну тут объяснения излишни
    action = input('''
    1 - Посчитать
    2 - Пойти нафиг  
    3 - cпой песню
    
    ''')
    if action == '1':
        x = input('Введите первое число')
        y = input('Введите 2ое число')
        try:
            x = float(x)
            y = float(y)
            action = input('''    
        введите действие:
        * - умножение 
        / - деление 
        +
        _
        q - выйти
            ''')
            if action in true_action:
                z = calculate(x=x, y=y, action=action)
                print(f'Ваш результат, {z}')
            elif action == 'q':
                break
            else:
                print('отстань я считаю,абобус')
        except:
            print("отстань я считаю,абобус")
    elif action == '2':
        print('Ну так иди нафиг!!!')
    elif action == '3':
        print('''Я сиренаголовый лалала
Убежать попробуй лалала
Тут и там ещё в городах лесах
Жертву я найду разорву по кускам

Жертву я найду ду ду ду ду
На куски порву ву ву ву ву
Жертву я найду ду ду ду ду
На куски порву ву разорву
И я поймаю тебя

Я поймаю тебя
Я тот самый стоун
Протоптал сотни троп
Мои сирены бомба действуют на все сто''')
        break