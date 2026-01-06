import random
def game(): 
    while True:
        try:
            difficulty=int(input('pls enter difficulty level as 1,2,3 and 4 to exit the game ,respectively!!\n1.Easy\n2.Mediam\n3.Hard\n4.Exit\n>>>>' ))
            if difficulty==1:
                l=10
                i=100
            elif difficulty==2:
                l=7
                i=500
            elif difficulty==3:
                l=5
                i=1000
            elif difficulty==4:
                print("thankyou")
                return 
        except ValueError:
            print('pls enter right value')
            continue
        

        n=random.randint(1,i)
        t=0
        while True:
            try:
                guess=int(input(('pls enter you guess>>>')))
            except ValueError:
                print('pls enter a interger only!!!!!')
                continue
            t+=1
            if guess==n:
                print("you won!!!")
                print(f'it took you {t} guesss!!')
                t=0    
                break
            if t>=l:
                print('you lost!!!!!')
                break
            if n>guess:
                if guess>n-100:
                    print('A little low!')
                else:
                    print('Too low!!')
            else:
                if guess<n+100:
                    print("A little high!")
                else:
                    print('Too high!!')
    
game()