import requests, os, colorama, json, time, threading, random, fade
from colorama import Fore

os.system("cls")
os.system("title Vanity Sniper - Made By LeyoZz")
vanity ="""
 __     __          _ _           ____        _                 
 \ \   / /_ _ _ __ (_) |_ _   _  / ___| _ __ (_)_ __   ___ _ __ 
  \ \ / / _` | '_ \| | __| | | | \___ \| '_ \| | '_ \ / _ \ '__|
   \ V / (_| | | | | | |_| |_| |  ___) | | | | | |_) |  __/ |   
    \_/ \__,_|_| |_|_|\__|\__, | |____/|_| |_|_| .__/ \___|_|   
                          |___/                |_| 

[1] WITH NO LOG CHANNEL
[2] WITH LOG CHANNEL
"""
fadervanity = fade.greenblue(vanity)
print(fadervanity)
choicererer = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}CHOICE YOUR NUMBER{Fore.WHITE}: ")
if choicererer=="01"or choicererer=="1":
    os.system("cls")
    vanity1 ="""
__     __          _ _           ____        _                 
\ \   / /_ _ _ __ (_) |_ _   _  / ___| _ __ (_)_ __   ___ _ __ 
 \ \ / / _` | '_ \| | __| | | | \___ \| '_ \| | '_ \ / _ \ '__|
  \ V / (_| | | | | | |_| |_| |  ___) | | | | | |_) |  __/ |   
   \_/ \__,_|_| |_|_|\__|\__, | |____/|_| |_|_| .__/ \___|_|   
                         |___/                |_| """
    fadervanity2 = fade.greenblue(vanity1)
    print(fadervanity2)
    howmuch = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}HOW MUCH CODES YOU WANT GENERATE (MAX 15){Fore.WHITE}: ")
    if howmuch =="1":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuch=="2":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuch=="3":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuch=="4":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee4})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuch=="5":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee4})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee5})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuch=="6":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee4})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee5})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee6})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuch=="7":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee4})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee5})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee6})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee7})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuch=="9":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee4})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee5})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee6})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee7})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee8})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee9})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")

    elif howmuch=="10":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee10 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee4})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee5})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee6})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee7})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee8})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee9})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee10 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee10})
                if(responseee10.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee10.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuch=="11":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee10 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee11 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee4})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee5})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee6})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee7})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee8})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee9})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee10 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee10})
                if(responseee10.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee10.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee11 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee11})
                if(responseee11.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee11.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuch=="12":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee10 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee11 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee12 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee4})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee5})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee6})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee7})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee8})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee9})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee10 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee10})
                if(responseee10.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee10.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee11 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee11})
                if(responseee11.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee11.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee12 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee12})
                if(responseee12.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee12.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuch=="13":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee10 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee11 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee12 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee13 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee4})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee5})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee6})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee7})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee8})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee9})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee10 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee10})
                if(responseee10.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee10.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee11 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee11})
                if(responseee11.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee11.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee12 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee12})
                if(responseee12.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee12.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee13 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee13})
                if(responseee13.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee13.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuch=="14":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee10 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee11 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee12 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee13 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee14 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee4})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee5})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee6})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee7})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee8})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee9})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee10 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee10})
                if(responseee10.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee10.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee11 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee11})
                if(responseee11.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee11.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee12 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee12})
                if(responseee12.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee12.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee13 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee13})
                if(responseee13.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee13.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee14 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee14})
                if(responseee14.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee14.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuch=="15":
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee10 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee11 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee12 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee13 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee14 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee15 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee4})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee5})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee6})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee7})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee8})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee9})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee10 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee10})
                if(responseee10.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee10.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee11 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee11})
                if(responseee11.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee11.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee12 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee12})
                if(responseee12.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee12.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee13 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee13})
                if(responseee13.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee13.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee14 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee14})
                if(responseee14.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee14.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee15 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee15})
                if(responseee15.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee15.status_code == 200):
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")


if choicererer =="02"or choicererer=="2":
    os.system("cls")
    vanity4 ="""
__     __          _ _           ____        _                 
\ \   / /_ _ _ __ (_) |_ _   _  / ___| _ __ (_)_ __   ___ _ __ 
 \ \ / / _` | '_ \| | __| | | | \___ \| '_ \| | '_ \ / _ \ '__|
  \ V / (_| | | | | | |_| |_| |  ___) | | | | | |_) |  __/ |   
   \_/ \__,_|_| |_|_|\__|\__, | |____/|_| |_|_| .__/ \___|_|   
                         |___/                |_| """
    fadervanity3 = fade.greenblue(vanity4)
    print(fadervanity3)
    howmuchcodes= input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}HOW MUCH VANITYS YOU WANT TO SNIPE (MAX 15){Fore.WHITE}: ")
    if howmuchcodes=="1":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="2":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                responsee = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(responsee.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="3":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="4":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee4}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="5":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee4}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee5}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="6":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee4}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee5}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee6}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="7":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee4}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee5}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee6}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee7}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="8":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee4}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee5}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee6}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee7}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee8}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="9":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee4}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee5}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee6}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee7}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee8}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee9}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="10":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee10 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee4}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee5}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee6}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee7}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee8}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee9}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee10 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee10.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee10.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee10}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="11":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee10 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee11 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee4}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee5}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee6}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee7}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee8}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee9}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee10 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee10.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee10.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee10}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee11 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee11.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee11.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee11}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="12":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee10 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee11 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee12 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee4}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee5}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee6}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee7}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee8}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee9}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee10 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee10.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee10.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee10}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee11 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee11.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee11.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee11}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee12 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee12.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee12.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee12}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="13":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee10 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee11 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee12 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee13 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee4}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee5}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee6}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee7}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee8}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee9}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee10 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee10.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee10.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee10}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee11 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee11.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee11.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee11}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee12 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee12.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee12.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee12}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee13 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee13.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee13.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee13}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="14":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee10 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee11 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee12 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee13 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee14 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee4}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee5}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee6}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee7}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee8}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee9}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee10 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee10.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee10.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee10}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee11 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee11.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee11.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee11}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee12 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee12.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee12.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee12}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee13 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee13.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee13.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee13}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee14 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee14.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee14.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee14}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
    elif howmuchcodes=="15":
        webhook = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT WEBHOOK HERE{Fore.WHITE}:")
        guildid = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PUT GUILD ID HERE{Fore.WHITE}: ")
        codee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee4 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee5 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee6 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee7 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee8 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee9 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee10 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee11 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee12 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee13 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee14 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        codeeee15 = input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}INPUT CODE HERE{Fore.WHITE}: ")
        print()
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            while True:
                headers={
                    "accept": "*/*",
                    "authorization": token,
                    "content-type": "application/json"
                }
                response = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codee})
                if(response.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(response.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responsee1 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeee})
                if(responsee1.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responsee1.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee2 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee})
                if(responseee2.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee2.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee4 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee4})
                if(responseee4.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee4.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee4}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee5 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee5})
                if(responseee5.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee5.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee5}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee6 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee6})
                if(responseee6.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee6.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee6}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee7 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee7})
                if(responseee7.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee7.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee7}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee8 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee8})
                if(responseee8.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee8.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee8}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee9 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee9})
                if(responseee9.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee9.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee9}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee10 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee10})
                if(responseee10.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee10.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee10}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee11 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee11})
                if(responseee11.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee11.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee11}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee12 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee12})
                if(responseee12.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee12.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee12}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee13 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee13})
                if(responseee13.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee13.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee13}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee14 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee14})
                if(responseee14.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee14.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee14}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")
                responseee15 = requests.patch(f"https://discord.com/api/v9/guilds/{guildid}/vanity-url", headers=headers, json={"code": codeeee15})
                if(responseee15.status_code == 400):
                    print(f"{Fore.WHITE}> {Fore.LIGHTRED_EX}THE VANITIY IS ALREADY OR TOKEN ARE NOT ON SERVER!{Fore.RESET}")
                else:
                    if(responseee15.status_code == 200):
                        print()
                        print(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}YOUR VANITY SNIPER {Fore.LIGHTGREEN_EX}SUCCESSFULLY {Fore.LIGHTCYAN_EX}SNIPED A VANITY!")
                        print()
                        e = f"""@everyone\n```DEV BY: LeyoZz\nSHOP: https://inspectservices.sellix.io\nSERVER: discord.gg/inspectservices```\n\nSUCCESSFULLY SNIPED VANITY: https://discord.gg/{codeeee15}"""
                        response232 = requests.post(webhook, headers={"authorization": token}, json={"content": e})
                        input(f"{Fore.WHITE}> {Fore.LIGHTCYAN_EX}PRESS ENTER AND LEAVE!")