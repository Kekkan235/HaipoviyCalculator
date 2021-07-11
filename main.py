print('*'*40 + 'Калькулятор' + "*"*40)
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
    print(f'чо надо абобус')
    action = input('''
    1 - Посчитать
    2 - Пойти нафиг  
    
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
        break