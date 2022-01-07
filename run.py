from os import system

tokens = open('tokens.txt').read().split('\n')
base_py = open('bot_layout.py', encoding='utf-8').read()

for index, token in enumerate(tokens):
    with open(f'bot_{index}.py', 'w', encoding='utf-8') as bot:
        bot.write(base_py.replace('insert token', token))
    system(f'start bot_{index}.py')
