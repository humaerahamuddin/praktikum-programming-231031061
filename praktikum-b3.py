print('praktikum-3 \n')
print('NAMA LENGKAP : Humaera Hamuddin')
print('NIM:231031061')
print('PRODI: sistem informasi B')

##########
a = True
b = False

print('\n==============NAND============')
hasil = not (a and a)
print (a, 'nand', a, 'adalah=', hasil)
hasil = not (a and b)
print (a, 'nand', b, 'adalah=', hasil )
hasil = not (b and a)
print (b, 'and', a, 'adalah=', hasil)
hasil = not (b and b)
print (b, 'nand', b, 'adalah=', hasil )

print('\n============NXOR============')
hasil = not (a ^ a)
print (a, 'nxor', a, 'adalah=', hasil)
hasil = not (a ^ b)
print (a, 'nxor', b, 'adalah=', hasil )
hasil = not (b ^ a)
print (b, 'nxor', a, 'adalah=', hasil)
hasil = not (b ^ b)
print (b, 'nxor', b, 'adalah=', hasil )


# INI OPERATOR MEMBERSHIP
print('\n============ IN ============')
nama = 'Humaera'

test = 'ma' #ISI dengan 2 huruf ada di nama 
cek = test in nama 
print(test,'ada di',nama,'adalah=',cek) 

test = 'am' #ISI dengan 2 huruf ada di nama 
cek = test in nama 
print(test,'ada di',nama,'adalah=',cek) 

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'


cek = test1 in nama
print(test1,'ada di',nama,'adalah=',cek) 
print()
cek = test2 in nama
print(test2,'ada di',nama,'adalah=',cek) 
print()
cek = test3 in nama
print(test3,'ada di',nama,'adalah=',cek) 
print()
cek = test4 in nama
print(test4,'ada di',nama,'adalah=',cek) 
print()
cek = test5 in nama
print(test5,'ada di',nama,'adalah=',cek)  
#lanjutkan kode 
print()
cek = not (test1 in nama)
print(test1,'tidak ada di',nama,'adalah=',cek) 
print()
cek = not (test2 in nama)
print(test2,'tidak ada di',nama,'adalah=',cek) 
print()
cek = not (test3 in nama)
print(test3,'tidak ada di',nama,'adalah=',cek) 
print()
cek = not (test4 in nama)
print(test4,'tidak ada di',nama,'adalah=',cek) 
print()
cek = not (test5 in nama)
print(test5,'tidak ada di', nama,'adalah=',cek)  
print()

#dengan cara yang sama buat operator not in 

# INI operator BTWISE 
print('\n')
a = 25 #tanggal lahir 
b = 12 #bulan lahir 
a += 60
b += 80
print('=========AND========')
print('Nilai',a,'biner adalah=',format(a,'09b'))
print('Nilai',b,'biner adalah=',format(a,'09b'))
print('-----------------------------------------------------AND')
C = a & b
print('Nilai',a,'&',b,'binner adalah=',format(C,'10b'))

print('=======OR=======')
#TUGAS buat or 
print ('nilai',a,'biner adlah=',format (a, '09'))
print ('nilai',b,'biner adlah=',format (b, '09'))
c = a | b
print ('nilai',a,'nor',b,'biner adalah=',format(c,'09b'))

print ('==========xor=======')
# tugas buat xor 
print ('nilai',a,'biner adlah=',format (a, '09'))
print ('nilai',b,'biner adlah=',format (b, '09'))
c = a ^ b
print ('nilai',a,'xor',b,'biner adalah=',format(c,'09b'))


print('\n=======NOT=======')
c = ~a 
print('Nilai',a,'biner adalah=',format(a,'09b'))
print('Nilai',a,'biner adalah=',format(a,'09b'))
#lanjutkan untuk not b
print('Nilai not',b,'biner adalah',format(c,'09b'))
print('Nilai not',b,'biner adalah',format(c,'09b'))


print('\n=======letf shift=======')
c = a << 2
print('Nilai',a,'biner adalah=',format(a,'09b'))
print('Nilai',a,'<< 2 biner adalah=',format(a,'09b'))
c = b << 2
print('Nilai',b,'biner adalah=',format(a,'09b'))
print('Nilai',b,'<< 2 biner adalah=',format(a,'09b'))

print('\n=======letf shift=======')
c = a >> 2
print('Nilai',a,'biner adalah=',format(a,'09b'))
print('Nilai',a,'>>2 biner adalah=',format(a,'09b'))
c = b >> 2
print('Nilai',b,'biner adalah=',format(a,'09b'))
print('Nilai',b,'>>2 biner adalah=',format(a,'09b'))

print('\n=======letf shift=======')
c = a << 2
print('Nilai',a,'biner adalah=',format(a,'09b'))
print('Nilai',a,'<< 2 biner adalah=',format(a,'09b'))
c = b << 2
print('Nilai',b,'biner adalah=',format(a,'09b'))
print('Nilai',b,'<< 2 biner adalah=',format(a,'09b'))

print('=========NOT AND========')
print('Nilai',a,'biner adalah=',format(a,'09b'))
print('Nilai',b,'biner adalah=',format(a,'09b'))
print('-----------------------------------------------------AND')
C = ~ (a & b)
print('Nilai',a,'&',b,'binner adalah=',format(C,'10b')) 

print('\n=======NOT OR======')
c = ~ (a|b)
print('Nilai',a,'biner adalah=',format(a,'09b'))
print('Nilai not',b,'biner adalah',format(c,'09b'))
print('Nilai',a,'&',b,'binner adalah=',format(C,'10b')) 


print('\n=======NOT XOR=====')
print ('nilai',a,'biner adlah=',format (a, '09'))
print ('nilai',b,'biner adlah=',format (b, '09'))
c = (a ^ b)
print ('nilai',a,'xor',b,'biner adalah=',format(c,'09b')) 

print ('\n=============NOT left shift===========')
c = ~ (a << 2)
print ('nilai', a, 'biner adalah=', format(a,'09b'))
print ('nilai', a, 'not','<< 2 biner adalah=', format(a,'09b'))
print ()
c = ~ (b << 2) 
print ('nilai', b, 'biner adalah=', format(a,'09b'))
print ('nilai', b, 'not', '<< 2 biner adalah=', format(a,'09b'))

print ()
print ('\n=============NOT right shift===========')
c = ~ (a >> 2) 
print ('nilai', a, 'biner adalah=', format(a,'09b'))
print ('nilai', a, 'not', '>> 2 biner adalah=', format(a,'09b'))
print ()
c = ~(b >> 2) 
print ('nilai', b, 'biner adalah=', format(a,'09b'))
print ('nilai', b, 'not','>> 2 biner adalah=', format(a,'09b'))






