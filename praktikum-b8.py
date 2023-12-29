import os
os.system('clear')

pwd_benar='si23b'
a = True
i = 0
Limit = 3
while a:
       pwd = input('Masukan Pasword:')
       if pwd == pwd_benar:
              print('selamat anda login!')
              a = False
else:
        if i == Limit:
            a = False 
            print('anda kehabisan kesempatan')
        
        else: 
            print('pasword salah!')
            

  