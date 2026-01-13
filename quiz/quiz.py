
quiz_data = [
    # 1️⃣ Questions with correct answers (dict)
    {
        "What is the SI unit of frequency?": "a",
        "Sound cannot travel through which medium?": "d",
        "Which of the following determines the pitch of a sound?": "b",
        "The speed of sound is maximum in:": "c",
        "What type of wave is a sound wave?": "a"
    },

    # 2️⃣ Options (list under a list)
    [
        ["a) Hertz", "b) Decibel", "c) Meter", "d) Second"],
        ["a) Solid", "b) Liquid", "c) Gas", "d) Vacuum"],
        ["a) Amplitude", "b) Frequency", "c) Speed", "d) Loudness"],
        ["a) Air", "b) Water", "c) Solids", "d) Vacuum"],
        ["a) Longitudinal wave", "b) Transverse wave", "c) Electromagnetic wave", "d) Light wave"]
    ],

    # 3️⃣ Explanations (list)
    [
        "Frequency is measured in Hertz (Hz).",
        "Sound cannot travel through vacuum.",
        "Pitch depends on the frequency of sound.",
        "Sound travels fastest in solids.",
        "Sound waves are longitudinal waves."
    ]
]
questions = quiz_data[0]
options = quiz_data[1]
explanations = quiz_data[2]

for c,key in enumerate(questions.keys()):
    while True:
        print(key)
        for i in options[c]:
            print(i)
        user_ans=input('pls enter your answer:')
        if user_ans not in ['a','b','c','d']:
            print('invalid input')
            continue
        if (questions[key].lower())==user_ans.lower():  
            print("that's the correct answer!!")
            print(explanations[c])
            break
        else:
            print('wrong answer!!!! ')
            retry=input('would you like to 1.retry or 2.explaination(pls answer as 1 or 2 accodingly)>>>')
            if retry==str(1):
                continue
            else:
                print(explanations[c])
                break
    


    
    
