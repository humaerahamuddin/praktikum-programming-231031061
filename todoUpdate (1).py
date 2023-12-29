import os , sys , time

file_path = "tugas.txt" #memasukan tugas.txt ke dalam file path
sp = 45

def tambah():
	tugas_baru = input(" Masukan Tugas Baru: ")
	with open(file_path,"a") as file: 
		file.write(tugas_baru + "\n")
		os.system("cls")
		print("-"*52)
		print("|".ljust(15)+"Tugas Baru Ditambahkan.".center(15)+"|".rjust(15))
		print("-"*52)
		
def lihat():
	try:		
		with open(file_path,"r") as file: 
			todo = file.readlines() 
			if not todo: 	
				os.system("cls")		
				print("-"*45)
				print("|".ljust(15)+"Tugas Kosong..".center(15)+"|".rjust(15))
				print("-"*45)
			else:
				os.system("cls")
				print("-"*45)
				print("|".ljust(15)+"Tugas".center(15)+"|".rjust(15))
				print("-"*45)
				for i,tugas in enumerate(todo, start=1): 
					print("|",i,"| "+(tugas.strip()).ljust(15))
				print("-"*45)
	except FileNotFoundError: 
		print("File tidak Ditemukan. Tambahkan Tugas terlebih dahulu .. yaa")

def edit():
	lihat()
	try: 	
		with open(file_path,"r") as file:	
			todo = file.readlines()		
		if not todo:
			print("Tidak ada tugas untuk diedit\n") 
			return 
		nomor_tugas = int(input("Masukan nomor tugas yang ingin di edit : ")) 
		if 1 <= nomor_tugas <= len(todo): 	
			tugas_baru = input("Masukan Tugas Baru : ") 
			todo[nomor_tugas -1] = tugas_baru + "\n" 	
			with open(file_path,"w") as file:
				file.writelines(todo)
			os.system("cls")
			print("-"*52) 		
			print("|".ljust(15)+"Tugas Berhasil di edit".center(15)+"|".rjust(15))
			print("-"*52) 
		else:
			os.system("cls")
			print("-"*53)
			print("|".ljust(15)+"Nomor tugas tidak valid.".center(15)+"|".rjust(15)) 
			print("-"*53)
	except ValueError:
		print("Masukan nomor tugas yang benar dong kaks")

def hapus():
	lihat()
	try:
		with open(file_path,"r") as file:
			todo = file.readlines() 
		if not todo:
			print("Tidak ada tugas untuk diedit\n")
			return 
		hapus_tugas = int(input("Masukan Nomor Tugas Yang Ingin Dihapus: "))
		if 1 <= hapus_tugas <= len(todo): 
			tugas_yg_dihapus = todo.pop(hapus_tugas - 1)
			with open(file_path,"w") as file:
				file.writelines(todo)
				os.system("cls")
				print("-"*53)
				print("|".ljust(15)+"Tugas Berhasil Dihapus..".center(15)+"|".rjust(15))
				print("-"*53)
		else:
			print("nomor tugas tidak valid..".title)
	except ValueError:
		print("Masukan nomor tugas yang benar dong kakak")

def hapusLangsung():
	try:
		os.system("cls")
		pilih = input("Yakin mau hapus semua ? (y/n)")
		if pilih == "y":
			os.remove(file_path)
			os.system("cls")
			print("-"*50)
			print("|".ljust(15)+"Tugas Sudah di hapus".center(15)+"|".rjust(15))
			print("-"*50)
		elif pilih == "n":
			os.system("cls")
			print("-"*50)
			print("|".ljust(15)+"Tugas Tidak di hapus".center(15)+"|".rjust(15))
			print("-"*50)
	except:
		print("file tidak di temukan")

def main():
	os.system("cls")
	while True:
		print("-"*45)
		print("|".ljust(0)+"Selamat Datang Di Program To-Do-List".center(43)+"|".rjust(-1))
		print("-"*45)
		print("|1.|".ljust(15)+"Tambah Tugas".center(15)+"|".rjust(15))
		print("|2.|".ljust(15)+"Lihat Tugas".center(15)+"|".rjust(15))
		print("|3.|".ljust(15)+"Edit Tugas".center(15)+"|".rjust(15))
		print("|4.|".ljust(15)+"Hapus Tugas".center(15)+"|".rjust(15))
		print("|5.|".ljust(15)+"Hapus Semua Tugas".center(15)+"|".rjust(13))
		print("|6.|".ljust(15)+"Exit".center(15)+"|".rjust(15))
		print("-"*45)
		print()
		pilihan = int(input("Pilihan Menu (1/2/3/4/5) : ")) #input untuk aksi selanjutnya

		if pilihan == 1:
			os.system("cls")
			tambah()
		elif pilihan == 2:
			lihat()
		elif pilihan == 3:
			edit()
		elif pilihan == 4:
			hapus()
		elif pilihan == 5:
			hapusLangsung()
		elif pilihan == 6:
			terima_kasih = "Terima Kasih ya kakak"
			os.system("cls")
			print("-"*51)
			print("|".ljust(15)+terima_kasih+"|".rjust(15))
			print("-"*51)
			sys.exit()
		else:
			print("masukan angka yg benar")

		kembali = input("Kembali ke menu utama (y/n) : ")
		os.system("cls")
		if kembali != "y":
			os.system("cls")
			print("-"*51)
			print("|".ljust(15)+"Terima Kasih Ya kakak"+"|".rjust(15))
			print("-"*51)
			break

			
if __name__ == '__main__': 				 
	if not os.path.exists(file_path): 
		with open(file_path, "w"):
			pass
	main()
