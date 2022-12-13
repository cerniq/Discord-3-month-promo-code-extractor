import asyncio
import ctypes
import sys
import aiohttp
import fade
import requests

claimed = 0

with open('tokens.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
globlines = len(lines)

print(fade.purpleblue("""                
                                     █
████ ████ █████ █████      █        █ 
█    █  █ █     █         █ █      █  
█  █ █    █████ █████    █   █    █   
█  █ █    █     █       █     █  █    
████ █    █████ █████  █       ██


░█████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░╚═╝██║░░██║██║░░╚═╝█████═╝░
██║░░██╗██║░░██║██║░░██╗██╔═██╗░
╚█████╔╝╚█████╔╝╚█████╔╝██║░╚██╗
░╚════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝

"""))

ctypes.windll.kernel32.SetConsoleTitleW(f'Haunt Xbox Code Claimer | Claimed: {claimed}')

def get_token():
    with open('tokens.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if(len(lines) > 0):
        return lines[0].strip()
    else:
        return False


def lol(code):
    with open("tokens.txt", "r") as f:
        lines = f.readlines()
    with open("tokens.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != code:
                f.write(line)

def get_code():
    token = get_token()
    if not token:
        sys.exit(fade.red("[!] No token found!"))
    headers = {
        'authorization': token
    }
    try:
        req = requests.post("https://discord.com/api/v9/outbound-promotions/890374599315980288/claim", headers=headers)
        r = req.json()
        global claimed
        claimed += 1
        lol(token)
        ctypes.windll.kernel32.SetConsoleTitleW(f'Haunt Xbox Code Claimer | Claimed: {claimed}')
        with open('output/codes.txt', 'r', encoding='utf-8') as f:
            lines = f.read()
        data = lines + r['code'] + '\n'
        with open('output/codes.txt', 'w', encoding='utf-8') as f:
            f.write(data)
        return r['code']
    except Exception as e:
        print((f"[!] {e}"))


while(globlines > 0):
    print(get_code())
    globlines -= 1
