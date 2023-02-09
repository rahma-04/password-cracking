#Client 2 Side
import xmlrpc.client
import time
import numpy as np
from collections import Counter
s = xmlrpc.client.ServerProxy('http://127.0.0.1:8000')
now = time.time()

print("Mengkoneksikan dengan server ..")

text_file = open("kamus.txt", "r")
lines = text_file.readlines()

for i in range(3000, 5999):
    ketemu = False
    s.getWordWorker(lines[i].strip())
    print(s.bruteforce())
  
    if s.bruteforce() == True:
        ketemu = True 
        print(f"Selamat kamu telah memecahkan password! Passwordnya adalah: {s.gotcha()}")
        break
    
if ketemu == False:
    print("Kamu gagal memecahkan password!")

print(f"Waktu eksekusi: {time.time()- now} detik")
