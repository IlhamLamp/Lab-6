import os, platform
import data

if(platform.system() == 'Windows'):
    os.system('cls')
else:
    os.system('clear')

while(True):

    print(" "*15,"======================================")
    print(" "*15,'|              PROGRAM               |')
    print(" "*15,'|       DAFTAR NILAI MAHASISWA       |')
    print(" "*15,"======================================")
    tanya = int(input("\n[1]Tambah , [2]Tampilkan , [3]Hapus , [4]Ubah , [5]Keluar : "))
    print("\n")

    if(tanya == 1):
        data.tambah()

    elif(tanya == 2):
        data.tampilkan()

    elif(tanya == 3):
        data.hapus()

    elif(tanya == 4):
        data.ubah()

    elif(tanya == 5):
        break

    else:
        print("Keyword yang anda masukkan salah ...")

    print("\n")
