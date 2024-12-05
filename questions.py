def welcome():
    print('Welcome to the test.')
    input('When you are ready press enter.')

def ask_questions(ask_color=False):
    name = input('name: ')
    print(f'It is nice to meet you {name}')

    if ask_color:
        color = input('What is your favorit color?')
        print(f'{color} is a great color!')

    input('Describle yourself')
    print('Admirable!')

def goodbye():
    print('Goodbye.')
    
welcome()
ask_questions()
goodbye()

welcome()
ask_questions(ask_color=True)
goodbye()