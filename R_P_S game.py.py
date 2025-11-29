import random
while True:
    f=[
        ['Draw','Win','Lose'],
        ['Lose',"Draw","Win"],
        ["Win","Lose",'Draw']
    ]

    userinput=(input(('pls enter a number\n 0 for rock!\n 1 for paper! \n 2 for sioser!\n or exit to leave the game :(\n>>>>')))
    reandom_compter=random.randint(0,2)
    if userinput.lower().strip() =='exit':
        print('thanks!! for playing the game see you next time!!!(;')
        break 
    userinput=int(userinput)
    options=['rock',
    'paper',
    'sioser']
    try:
        print(f'computer choose {options[reandom_compter]} you {f[userinput][reandom_compter]}!!!!!!!!!!!!!!!!!!!') 
    except:
        print('invalid input!!!!!')