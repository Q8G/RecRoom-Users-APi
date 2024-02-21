from datetime import datetime
from colorama import init, Fore
import ctypes, threading, requests, json, time

init()

def title_update():
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW("Rec Room Users Api > 1.0v > Github/Q8G")
        time.sleep(1)
        ctypes.windll.kernel32.SetConsoleTitleW("Rec Room Users Api >> 1.0v >> Github/Q8G")
        time.sleep(1)
        ctypes.windll.kernel32.SetConsoleTitleW("Rec Room Users Api >>> 1.0v >>> Github/Q8G")
        time.sleep(1)

def read_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.text.strip():
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as err:
        print(err)

def tool():
    url = input(Fore.CYAN + " RecRoom Username: " + Fore.YELLOW)
    print(Fore.RESET)
    url1 = f"https://apim.rec.net/accounts/account?username={url}"
    website_content = read_website_content(url1)

    if website_content is not None:
        data = json.loads(website_content)
        account_id = data.get('accountId')
        username = data.get('username')
        displayName = data.get('displayName')
        url2 = f"https://apim.rec.net/accounts/account/{account_id}/bio"
        website_content1 = read_website_content(url2)
        data1 = json.loads(website_content1)
        Bio = data1.get('bio')
        url3 = f"https://clubs.rec.net/subscription/subscriberCount/{account_id}"
        website_content2 = read_website_content(url3)
        data2 = json.loads(website_content2)
        profileImage = data.get('profileImage')
        bannerImage = data.get('bannerImage')
        createdAt = data.get('createdAt')
        createdAt1 = str(createdAt)[:4]
        createdAt2 = str(createdAt)[5:7]
        if createdAt2.startswith('0'):
            createdAt2 = int(createdAt2)
        createdAt3 = str(createdAt)[8:10]
        if createdAt3.startswith('0'):
            createdAt3 = int(createdAt3)

        def calculate_time_difference(year, month, day):
            specified_date = datetime(year, month, day)
            current_date = datetime.now()
            time_difference = current_date - specified_date
            years = time_difference.days // 365
            months = (time_difference.days % 365) // 30
            days = (time_difference.days % 365) % 30
            return years, months, days

        result_years, result_months, result_days = calculate_time_difference(int(createdAt1), int(createdAt2), int(createdAt3))
        resy = f"{result_years} years, {result_months} months, and {result_days} days"

        isJunior = data.get('isJunior')
        print(Fore.RESET + f" ==================" + Fore.GREEN + " @Q8G " + Fore.RESET + "==================")
        print(Fore.LIGHTMAGENTA_EX + f"\n\n ID: " + Fore.GREEN + f"{account_id}\n")
        print(Fore.LIGHTMAGENTA_EX + f"\n\n Username: " + Fore.GREEN + f"@{username}\n")
        print(Fore.LIGHTMAGENTA_EX + f"\n\n Display Name: " + Fore.GREEN + f"{displayName}\n")
        print(Fore.LIGHTMAGENTA_EX + f"\n\n Bio: " + Fore.GREEN + f"{Bio}\n")
        print(Fore.LIGHTMAGENTA_EX + f"\n\n pfp url: " + Fore.GREEN + f"https://img.rec.net/{profileImage}\n")
        print(Fore.LIGHTMAGENTA_EX + f"\n\n banner url: " + Fore.GREEN + f"https://img.rec.net/{bannerImage}\n")
        print(Fore.LIGHTMAGENTA_EX + f"\n\n Subscribers: " + Fore.GREEN + f"{data2}\n")
        print(Fore.LIGHTMAGENTA_EX + f"\n\n since: " + Fore.GREEN + f"{resy}\n")
        print(Fore.LIGHTMAGENTA_EX + f"\n\n Date the account was created: " + Fore.GREEN + f"{createdAt1}-{createdAt2}-{createdAt3}\n")
        is_junior_text = "Yes" if isJunior else "No"
        print(Fore.LIGHTMAGENTA_EX + f"\n\n Junior Account: " + Fore.GREEN + f"{is_junior_text}\n\n")
        print(Fore.RESET + f" ===================" + Fore.RED + " End " + Fore.RESET + f"==================\n")
        again()
    else:
        print(Fore.RED + f" Not Found" + Fore.RESET)

def again():
    Again = input(Fore.MAGENTA + " You want to see another account? [" + Fore.LIGHTGREEN_EX + "Y" + Fore.MAGENTA + "/" + Fore.LIGHTRED_EX + "n" + Fore.MAGENTA + "]: " + Fore.RESET)
    print("")
    if 'Y' in Again or 'y' in Again:
        tool()
    elif 'n' in Again or 'N' in Again:
        exit()
    else:
        again()

title_thread = threading.Thread(target=title_update)
title_thread.start()

tool()
