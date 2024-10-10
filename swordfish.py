while True:
    print('Who are you?')
    name = input()
    if name != 'Alex':
        continue
    print('Hello Alex. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
    print('Access Granted, Welcome Friend!')
    