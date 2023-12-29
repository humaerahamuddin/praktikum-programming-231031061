import os
os.system('clear')

nim =[2,3,1,0,3,1,0,6,1]
print(nim)
# akses item
print('item indeks 0:',nim[0])
print('item indeks 3:',nim[3])
print('item indeks terakhir:',nim[len(nim)-1])
# akses indeks negatif 
print('item indeks terakhir:',nim[-1])
print('item indeks terakhir:',nim[-len(nim)])
print('item indeks 3: [-6]',nim[-6])
print('item indeks 5: [-4]',nim[-4])
print('item indeks -7: [2]',nim[2])
print('item indeks 2: [-7]',nim[-7])
# akses indeks batas 
print (f'item indeks 1,2....:{nim[3:]}')
print (f'item indeks 3,4....:{nim[3:]}')
print (f'item indeks 0,1,2,3....:{nim[:4]}')
print (f'item indeks 0:....:{nim[1:]}')
print (f'item indeks semua:....:{nim[:]}')
print (f'item indeks  [:8]:....:{nim[:-1]}')
print (f'item indeks  [:4]:....:{nim[:-5]}')
# pengirisan 
print (f'item indeks  1,2 {nim[1:3]}')
print (f'item indeks   []: {nim[3:3]}')
print (f'item indeks  2,3,4: {nim[2:5]}')
print (f'item indeks   [1:8]: {nim[1:-1]}')
print (f'item indeks   [2:7]: {nim[2:-2]}')
# Nested list
kelas = [('Matkul1',2)] [('matkul2,3')]
print(kelas)
kelas.append(('matkul3',2))
print(kelas)
#tambahkan matkul 4 dan 5 dan sksnya 

# Mata kuliah 1: Matkul1 degan 2 sks
# Mata kuliah 2: Matkul1 degan 3 sks
# Mata kuliah 3: Matkul1 degan 2 sks
# Mata kuliah 4: Matkul1 degan ..sks
# Mata kuliah 5: Matkul1 degan ..sks
data = [('Humaera Hamuddin',2023,'Aktif'),
        (98,99,99,97,98),
        (2,3,2,2,2),
        ('SI-Reguler','Sistem Informasi B','Ganjil')]

# tambahkan matkul 4 dan 5 dan sksnya
print ()
print (f'mata kuliah 1: {kelas[0][0]} dengan {kelas[0][1]} sks')
# Mata kuliah 1: Matkul1 dengan 2 sks
print (f'mata kuliah 2: {kelas[1][0]} dengan {kelas[1][1]} sks')
# Mata kuliah 2: Matkul2 dengan 3 sks
print (f'mata kuliah 3: {kelas[2][0]} dengan {kelas[2][1]} sks')
# Mata kuliah 3: Matkul3 dengan 2 sks
print (f'mata kuliah 4: {kelas[3][0]} dengan {kelas[3][1]} sks')
# Mata kuliah 4: Matkul4 dengan ... sks
print (f'mata kuliah 5: {kelas[4][0]} dengan {kelas[4][1]} sks')
# Mata kuliah 5: Matkul5 dengan ... sks

data = [('Humaera Hamuddin',2023,'Aktif'),
        (98,99,99,97,98),
        (2,3,2,2,2),
        ('SI-Reguler','Sistem Informasi B','Ganjil')]
print ()
print (f'nama mahasiswa : {data[0][0]}')
print ()
print (f'nama mahasiswa : {data[0][0]}')
# nama mahasiswa : Humaera Hamuddin
print (f'insial {data[0][0]} : {data[0][0][0]}')
# Inisial Humaera  : H
nim_int = int("".join(map(str,nim)))
print (f'NIM {data[0][0]}: {nim_int}')
# NIM Humaera Hamuddin : 231031061
print (f'program {data[0][0]}: {data[3][0]} {data[3][1]}')
# Program Humaera Hamuddin : S1-Reguler Sistem Informasi B
print (f'angkatan {data[0][0]}: {data [3][2]}-{data[0][1]}')
# Angkatan Humaera Hamuddin : Ganjil-2023
print (f'total sks {data[0][0]} adalah: {sum(data[2])}')
# Total sks Humaera Hamuddin adalah: 11 
print (f'jumlah nilai {data[0][0]}: {len(data[1])}')
# Jumlah Nilai Humaera Hamuddin : 5 
print (f'nilai tertinngi {data[0][0]}: {max(data[1])}')
# Nilai tertinggi Humaera Hamuddin: 99 
print (f'nilai terendah {data[0][0]}:{min(data[1])}')
# Nilai terendah Humaera Hamuddin : 97 
x_bar = sum(data[1])/len(data[1]) 
print (f'rata rata nilai {data[0][0]} : {x_bar}')
# Rata-rata nilai Humaera Hamddin: 92.8  