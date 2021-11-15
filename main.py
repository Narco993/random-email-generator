import random
import time
import string



print("[!] Gen was proudly coded by jxd/Landen/Narco")
print("[!] Don't skid")



num = int(input('[+] E-mails: '))
start = input("[!] Enter anything to start")

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))


for i in range(num):
 print ("[+] Email : ", random_char(16)+"@gmail.com  | " "  [+] Email :", random_char(16)+"@gmail.com", file=open('logs.txt', 'a'))

print("[+] Done generating E-mails")
time.sleep(500.2)
