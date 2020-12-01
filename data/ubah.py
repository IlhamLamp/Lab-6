from data import mahasiswa

#mengubah daftar mahasiswa
def ubah():
    nama = input("Masukkan nama mahasiswa untuk merubah data : ")
    if nama in mahasiswa.keys():
        print("-> Mau merubah apa ?")
        tanya = input("-> (semua), (nim), (tugas), (uts), (uas) : ")
        if tanya.lower() == "semua":
            print("+++ Mulai mengubah data {} +++".format(nama))
            mahasiswa[nama][1] = input("Ubah NIM  : ")
            mahasiswa[nama][2] = input("Ubah nilai tugas : ")
            mahasiswa[nama][3] = input("Ubah nilai uts   : ")
            mahasiswa[nama][4] = input("Ubah nilai uas   : ")
            mahasiswa[nama][5] = int(mahasiswa[nama][2])*30/100 + int(mahasiswa[nama][3])*35/100 + int(mahasiswa[nama][4])*35/100
            print("-> Data berhasil diubah!")
        elif tanya.lower() == "nim":
            mahasiswa[nama][1] = input("Ubah NIM : ")
            print("-> NIM berhasil diubah!")
        elif tanya.lower() == "tugas":
            mahasiswa[nama][2] = input("Ubah nilai tugas : ")
            mahasiswa[nama][5] = int(mahasiswa[nama][2])*30/100 + int(mahasiswa[nama][3])*35/100 + int(mahasiswa[nama][4])*35/100
            print("-> Nilai tugas berhasil diubah!")
        elif tanya.lower() == "uts":
            mahasiswa[nama][3] = input("Ubah nilai uts :")
            mahasiswa[nama][5] = int(mahasiswa[nama][2])*30/100 + int(mahasiswa[nama][3])*35/100 + int(mahasiswa[nama][4])*35/100
            print("-> Nilai UTS berhasil diubah!")
        elif tanya.lower() == "uas":
            mahasiswa[nama][4] = input("Ubah nilai uas : ")
            mahasiswa[nama][5] = int(mahasiswa[nama][2])*30/100 + int(mahasiswa[nama][3])*35/100 + int(mahasiswa[nama][4])*35/100
            print("-> Nilai UAS berhasil diubah!")
        else:
            print("-> Keyword yang anda masukkan salah ...")
    else:
        print("-> Mahasiswa {} tidak ditemukan".format(nama))
