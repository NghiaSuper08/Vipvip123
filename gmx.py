import requests
import os
import sys
import random
import threading

os.system('cls' if os.name == 'nt' else 'clear')

print("BOX ZALO: https://zalo.me/g/jgyotm477")
file_name = input("_NHẬP_FILE_CHỨA_MAIL_: ")
file_proxy = input("_NHẬP_FILE_CHỨA_PROXIES_: ")

with open(file_proxy) as file:
    proxies = file.read().splitlines()

def check_email(m, proxy):
    checkpro = {
        'http':f'http://{proxy}',
        'https':f'https://{proxy}',
    }
    gmx = requests.get('https://www.gmx.de/', params={'email': m}, proxies=checkpro)
    if gmx.status_code == 200:
        print("\033[1;37m(\033[1;31mLIVE\033[1;37m) {m}")
    elif gmx.status_code == 404:
        print(f"\033[1;37m(\033[1;32mDIE\033[1;37m) {m}")
    elif gmx.status_code == 403:
        print("\033[1;37m(\033[1;33mBlock Requests\033[1;37m) {m}")
    else:
        print("\033[1;37m(\033[1;34mERROR\033[1;37m) {m}")

threads = []
for proxy in proxies:
    with open(file_name) as file:
        mails = file.read().splitlines()
    for mail in mails:
        m = mail.strip("\n")
        t = threading.Thread(target=check_email, args=(m, proxy))
        threads.append(t)
        t.start()

for thread in threads:
    thread.join()
