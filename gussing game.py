while True:  
    import random
    mode=input('pls enter 1,2,3 as \n1.easy\n2.Medium\n3.hard \n>>>>>>>')
    easy=[    "cat", "dog", "ball", "tree", "book", "pen", "cup", "sun", "moon", "star",
    "fish", "car", "shoe", "bag", "door", "chair", "table", "apple", "milk", "water",
    "phone", "bed", "light", "bird", "smile", "rain", "flower", "clock", "spoon", "shoe"]
    medium=["pillow", "market", "window", "laptop", "garden", "bottle", "camera", "pocket", "cushion", "charger",
    "jungle", "mirror", "pillow", "bridge", "river", "button", "yellow", "purple", "battery", "planet",
    "rocket", "magnet", "powder", "travel", "butter", "switch", "silver", "cotton", "wallet", "desert"]
    hard=[ "velocity", "umbrella", "oxygen", "telescope", "monastery", "horizon", "galaxy", "emerald", "triangle", "compass",
    "fragment", "cylinder", "sequence", "organism", "eclipse", "altitude", "quantum", "parallel", "labyrinth", "spectrum",
    "inertia", "camouflage", "avalanche", "turbulence", "nebula", "antibody", "peninsula", "evolution", "symmetry", "parchment"]
    if mode=='1':
        word=random.choice(easy)
    elif mode=='2':
        word=random.choice(medium)
    elif mode=='3':
        word=random.choice(hard)
    else:
        print('worng input!!!!!')
        continue


    len_word=len(word)
    attempt=0
    while True:
        gusses=input(f'pls enter a guess of lenght {len_word} or if you want to give up make this pattern {{(*_*)}}:')
        if gusses=="(*_*)" :
            print(f'the word was >>{word}')
            break
        if len(gusses)!=len_word:
            print('pls enter the word in coorrect lenght!!!!!!!!!!!')
            continue
        if gusses==word:
            print(f'you did it!{{in {attempt} attempts !!!}}')
            break
        correct_letters=0
        correct_place=0
        
        for i in range(len_word):
            if gusses[i] in word:
                correct_letters+=1
            if gusses[i]==word[i]:
                correct_place+=1
       
        attempt+=1
        print(f'in this guess you did {correct_letters} latters correct and {correct_place} latters right in postion')



