import os
os.system('clear')


a = True

while a:
        jawab= input('Apakah ingin lanjutkan? (y/n)')
        if jawab == 'y':
                print('selamat Datang Lagi')
                
        elif jawab == 'n':
           print('sampai ketemu lagi :D')  
        a = False
        
else:
            os.system('clear')
            print('jagan aneh-aneh deh :).')
            a = True 