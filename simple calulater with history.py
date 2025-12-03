while True:
    userinput=input("enter a equeation,history,exit,clear:".upper()).strip().lower()
    if userinput == "history":
        with open ('data.txt','r') as r:
            his=r.readlines()
            if his:

                for i in his :
                    print(i)
            else:
                print('no histry found ')
    elif userinput == 'exit':
        print('good bye!!!!!! SEE  YOU NEXT TIME !!(:')
        break 
    elif userinput=='clear':
        with open ('data.txt','w') as c:
            pass
        print('history cleared!!!')
    else:
        try:
            ans=eval(userinput)
            print(ans)
            with open("data.txt",'a+') as f:
                if his:
                    f.seek(0)
                    lines = f.readlines()
                    first_char = int(lines[-1].strip()[0])
                    # print(first_char)

                    f.write(f'{first_char+1}.{userinput}={ans}\n')
                else:
                    f.write(f'1.{userinput}={ans}\n')


        except:
            print('unetical input!!!')
