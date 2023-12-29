import os 
os.system ('clear')

#judul
print ('program menghitung volume dab luas permukaan'.center(45))
print ('bangun ruang balok'.center(45))
print ()

#inputan 
panjang = float (input ('masukkan panjang: '))
lebar   = float (input ('masukkan lebar: '))
tinggi  = float (input ('masukkan tinggi: '))

#hitungan 
vol = p*l*t
luas_surf      = 2*(p*l + p*t + l*t)
luas_non_tutup = luas_surf - p*l 

#tampilan 
print (f'hasil perhitungan nilai volume : {vol}')
print (f'hasil perhitungan nilai luas permukaan : {luas_surf}')
print (f'hasil perhitungan nilai luas permukaan non tutup : {luas_non_tutup}')