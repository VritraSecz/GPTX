#!/bin/python3
# https://github.com/VritraSecz
# Code By: VritraSecz
# Don't be copycat create your own

import openai
import os
from time import sleep
from key import *

def exift():
    print()
    print("\033[1;91m[+]\033[1;92m Thanks for using \033[1;91mGPTX")
    sleep(0.14)
    print("\033[1;91m[~]\033[1;92m Don't Forget to follow us on socialmedia")
    sleep(0.14)
    print("\033[1;91m[~]\033[1;92m YouTube:\033[1;94m https://youtube.com/@Technolex")
    sleep(0.14)
    print("\033[1;91m[~]\033[1;92m Telegram:\033[1;94m https://t.me/LinkCentralX")
    sleep(0.14)
    print("\033[1;91m[~]\033[1;92m Github:\033[1;94m https://github.com/VritraSecz\n")
    sleep(0.14)

os.system('cat banr')
print("\n\033[1;91m[+] \033[1;92mAsk here whatever you want. To Exit just use \033[1;91mexit \033[1;92mor\033[1;91m bye\033[1;92m command.\n")

while True:
    askx = input("\033[1;91m][\033[1;97mYou\033[1;91m]> \033[1;92m")

    if askx == 'exit' or askx == 'bye':
        exift()
        break
    if askx == '':
        pass
    else:
        try:
            openai.api_key = (key) 
        
            response = openai.Completion.create(
                                    model='gpt-3.5-turbo-instruct',
                                    prompt=askx,
                                    max_tokens=3048,
                                    top_p=1.0,
            presence_penalty=0.0)

            print("\n\033[1;91m][\033[1;97mGPTX\033[1;91m]>\033[1;92m " + response.choices[0].text + "\n") # type:ignore
        except Exception as e:
            print(e)
