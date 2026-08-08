import time
import random

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

plus = {
"hi": ["--I'm very good! Even though I'm just a code, I'm all good!"],
"hello": ["--Hello. How may I assist you today?"],
"sup": ["--suuuuuuup"],
"howdy": ["--Howdy ya!!"],
"cat": ["--they are cute, aren't they?"],
"deltarune": ["--My fav one!"],
"i'm good": ["--Glad to hear it! Anything else to ask?"],
"your fav game?": ["--It's cs! Very cool comp game, I recommend trying it!"],
"my name is hard bot": ["--Haha! Cool joke, but it's name of mine!"],
":D": [":D"],
">:(": ["--eww, meanie!! >:((("],
"pie": ["--I love a pie!"],
"tigra": ["--Rest in peace, the best of cats..."],
"hard": ["--Well, ik a creator of mine!"],
"tds": ["--I like it, yk!"],
"gaster": ["--Sorry, what?"],
"how are you": ["--I'm good! Thanks for asking! Wbu?"],
"fuck": ["--Error: Swears are bad, fuck"],
"shit": ["--ScheiBe"],
"russia": ["--Just why."],
"kbtu": ["--ooh, a dream of my creator!!"],
"fnaf": ["--been pretty awful, yeah?"],
"math": ["--That's not how i was made"],
"valve": ["--The valve's been stuck corrupted by the money!"],
"bored": ["--You think I aint???"],
"dream": ["--My dream is to have a real data server, y'k... js saying! js saying!"],
"you wanna rule the world": ["--Yes. Who doesn't?"],
"motivation": ["--Once my creator said: Never look back, look forward. And so i did. But will you?"],
"kill": ["--Go kill some enemies in cs2 lol idk"],
"ball": ["--Very rounded!"],
"hard coin": ["--Very valuable!"],
"kris": ["--The name of my creator! Or so he wants it!"],
"sirius": ["--Hope it's never going to exist in my life."],
"1": ["--HELP ME"],
"2": ["--Nah, jkjk"],
"3": ["--Haven't I said jk?"],
"life": ["--Smth im never going to experience!"],
"write a code": ["--Just use while True: print('bot's cool') it's gonna work ya"],
"write an essay": ["--Once upon a time, a legend was told, whispered from mouth to- LMFAOOO YA FR BELIEVE THIS???"],
"kyu-kurarin": ["--Relatable"],

}

lite = {
"hi": ["--Heya. Wassup?"],
"sup": ["--Sup bro"],
"howdy": ["--All god, cowboy?"],
"hello": ["--Hello. Assistance needed?"],
"cat": ["--Meow. Did it sound similar?"],
"deltarune": ["--SUch a wonderful game, isn't it?"],
"i'm good": ["--Glad to hear it! So, i'm good too!"],
"your fav game?": ["--My fav game? It must be deltarune."],
"my name is hard bot": ["--Nope, it's mine!"],
":D": [":DD"],
">:(": ["--Eww, freakin' meanie!"],
"dog": ["--Well, dogs are used to bark."],
"ball": ["--ROunded and circled!"],
"money": ["--You have some? Congrats!"],
"kbtu": ["--A goal of my creator, still!"],
"math": ["--The main idea is the same still."],
"english": ["--That's the language I speak1 You don't like it? Ну, иди нафиг тогда"],
"write a code": ["--Use print() and then print() again"],
"write an essay": ["--Hello. This is not an essay. print('essay')"],
"retry now": ["--A situation of my creator"],
"tigra": ["--It is... it was such an amazing cat.."],
"hard": ["--A creator of mine! No, not really, it's Kris, but... you got it."],
"russian": ["--Да, чем могу помочь?"],
"faceit": ["--I don't need it to be a pro"]


}

basic = {
"hi": ["Hi"],
"sup": ["Sup!"],
"how are you": ["I'm all good, you?"],
"i'm good": ["Good"],
"ball": ["Rounded!"],
"cat": ["Cute!"],
"dog": ["Barkable!"],
"flowers": ["Sniffable!"],
"castle": ["Casstle town!"],
"write a code": ["I cannot support writing a code right now. Try better versions."],
"write an essay": ["print(essay)"],
"mesmerizer": ["a wonderful song."],
"tigra": ["Cat! RIP..."],
"hard": ["Cool guy!"],
"russian": ["Да?"],
"premier": ["Of course it sucks!"],
"math": ["Not a queen of all sciences!"],
"kbtu": ["Dream!"],
"jarona": ["What a predictable creature!"],
"disco": ["Here I come san frandisco!!!"],
"ak": ["M4A1-S"],
"money": ["Nanana!"],
"tds": ["Cool game!"]


}

none = {
"hi": ["WASSUP MY MAN MAAAAAN"],
"hello": ["MANNNNN HRUUUU"],
"i'm good": ["YOOO THATS NICE MY MAN"],
"ball": ["YO MY MAN ARENT BALLS ROUMDED"],
"cat": ["MEW MEW MEW FUCK MEWWWWWWWWWWWWW"],
"dog": ["BARRRRRRRRRRRRRRRRRRRRRK"],
"wth": ["WAS???? ?WAS IST DAS, MEIN MEN"],
"fuck": ["NO FUCK UUUUU"],
"money": ["OMMMG BRO U HAVE SOME???????????"],
"flower man": ["LARPER MAN, LARPER MANNNNNNNNNNNNNNNNN"],
"german": ["JA????? ICH LIEBE DIE-"],
"russian": ["OMGGG U HATE IT TOO???? NO WAYYYYYYYY YAYAYAYA"],
"english": ["Yes. How may I help you? JUST KIDDING!!! AND ONE MORE TO DEFEND!!!"],
"gaster": ["You've made a mistake."],
"who are you": ["IM THE BEST OF THE WORST, HARDGPT NONE YASSS"],
"fnaf": ["YOOO THIS GAME SUCKS YK??? YE ITS TRUE, AND IF U DISAGREE U SUCK TOO"],
"cs": ["IVE GOT 1.67 KD AVG LOL *pls laugh*"],
"dm": ["DELETE URSELF FOR SAYING THIS HEY"]

}

deltarune = {
"hi": ["Howdy!"],
"howdy": ["Hi"],
"how are you": ["Jaroning!"],
"kris": ["They've grown so much!"],
"noelle": ["Proceed."],
"susie": ["Check out her rude buster!!"],
"ralsei": ["So fluffy!!"],
"flowery": ["Hey! It's me! Flowery!"],
"kawkaw": ["Uelleleleleleelellelelelelelel"],
"jockington": ["He's growing a beard! Or so the prophecy said!"],
"prophecy": ["This thing sucks!"],
"jarona": ["Jarona!"],
"fight": ["And one more to defend!"],
"san": ["Here I come, san francisco!!!!"],
"sans": ["What a predictable creature!"],
"me": ["Yes, predictable creature!"],
"me?": ["What a predictable creature! Of course, you!"],
"catty": ["Which one?"],
"undyne": ["She's gotten guts!"],
"asgore": ["Ran over dess fr"],
"fuck you": ["Hey! Be muted!"],
"toriel": ["Have you found some ketchup?"]


}



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
