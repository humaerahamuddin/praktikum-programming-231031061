import os 
os.system('clear')

nama = 'Humaera Hamuddin'
nim  = '23103161'
meet = 'praktikum 4'
prodi = 'sistem inofrmasi B'
email = 'humaerahamuddin@gmail.com'  
tgl = '11 oktober 2023'
sp = 44
# print(len(nama))
print ('-'*sp)
print (nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(prodi.rjust(sp)) + f'\r{meet}'
#print(prodi.rjust(sp))
print(email.rjust(sp)+f'\{tgl}')
print('-'*sp)

paragraf = '''Halo, selamat datang pereknalkan 
nama saya {} dengan Nim {} dari prodi {}. 
ini adalah file {}.'''
p = paragraf.format(nama,nim,prodi,meet)
print(p)

#--------8++++++++
x = 9 #input 
hasil = x>8
print (x,'hasilnya adalah,hasil')
#--------8++++++++
x = 9 #input 
hasil = x<8
print (x,'hasilnya adalah,hasil')

print('-----------4++++++++8---------')
x = 9
#cek 1 = x>4 true 
cek1 = x>4
#cek 2 = x<8 true 
cek2 = x<8 
#hasil = cek1 and cek 2 -->true 
hasil = cek1 and cek2
print(x,'hasilnya adalah',hasil)

print('-----------4++++++++8---------')
x = 9
#cek 1 = x>4 true 
cek1 = x>4
#cek 2 = x<8 true 
cek2 = x<8 
#hasil = cek1 and cek 2 -->true 
hasil = cek1 or  cek2
print(x,'hasilnya adalah',hasil) 

print('-----------4++++++++8---------')
x = 2
#cek 1 = x>4 true 
cek1 = x>4
#cek 2 = x<8 true 
cek2 = x<8 
#hasil = cek1 and cek 2 -->true 
hasil = cek1 or  cek2
print(x,'hasilnya adalah',hasil) 

