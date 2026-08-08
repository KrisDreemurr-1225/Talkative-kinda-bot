import time
import random

from plus import plus

from lite import lite

from basic import basic

from none import none

from deltarune import deltarune

print("Welcome to hard bot gpt free 1.0!")
mode = int(input("""Select a mode.
1. HardGPT Plus(The best model we've made so far! Or is it???)
2. HardGPT lite(The common one!)
3. HardGPT basic(The most basic and boring model!)
4. FlowerGPT(The best model to ask for some deltarunings! Are there any other models...?) """))
time.sleep(1)
if mode == 1:
    print("Understood, HardGPT plus is on")
elif mode == 2:
    print("Understood, HardGPT lite is on")
elif mode == 3:
    print("Understood, HardGPT basic is on")
elif mode == 4:
    print("Jaronastood!")
else:
    print("Understood, HardGPT none is on")

greetings_phrase = [
"I'm ready to turn in!",
"I'm saying good evening!",
"I'm ready to help!",
"I'm just chilling in the void!"
]

time.sleep(2)
print(random.choice(greetings_phrase))

random_answers = [
"--what a predictable creature!",
"--uhhhh my generation broke lol",
"--okay?",
"--what is a life if not a pie?",
"--omgggg so relatable istggg"
]

none_answers = [
"YO BRO NO WAY",
"OMG FR???",
"YEAH IK ITS SICK",
"WOAH OMG CONGRATS"
]

random_deltarune = [
"--HOW'D YOU LIKE MY JARONA???",
"--What a predictable creature!",
"--Your dad's my best friend!",
"--Kriselle is the knight yk"
]

while True:

    if mode == 1:
        time.sleep(2)
        user = input("""Ask hard bot something!

enter your message here =   """).lower()


        if user in plus:
            print("""

Generating an answer...""")

            time.sleep(2)
            for line in plus[user]:
                print(line)

        else:
            print("""

Generating a worse answer...""")
            time.sleep(2)
            print(random.choice(random_answers))

    elif mode == 2:
        time.sleep(2)
        user_1 = input("""Ask hard bot something!

enter your message here =   """).lower()


        if user_1 in lite:
            print("""

Generating an answer...""")

            time.sleep(2)
            for line in lite[user_1]:
                print(line)


        else:
            print("""

Generating a worse answer...""")
            time.sleep(2)
            print(random.choice(random_answers))

    elif mode == 3:
        time.sleep(2)
        user_2 = input("""Ask hard bot something!

enter your message here =   """).lower()


        if user_2 in basic:
            print("""

Generating an answer...""")

            time.sleep(2)
            for line in basic[user_2]:
                print(line)


        else:
            print("""

Generating a worse answer...""")
            time.sleep(2)
            print(random.choice(random_answers))


    elif mode == 4:
        time.sleep(2)
        user_jarona = input("""Ask flowery bot something!

enter your message here =   """).lower()


        if user_jarona in deltarune:
            print("""

Generating an answer...""")

            time.sleep(2)
            for line in deltarune[user_jarona]:
                print(line)


        else:
            print("""

Generating a JARONING answer...""")
            time.sleep(2)
            print(random.choice(random_deltarune))

    else:
        time.sleep(2)
        user_3 = input("""Ask hard bot something!

enter your message here =   """).lower()


        if user_3 in none:
            print("""

Generating an answer...""")

            time.sleep(2)
            for line in none[user_3]:
                print(line)


        else:
            print("""

Generating an amazing answer...""")
            time.sleep(2)
            print(random.choice(none_answers))
