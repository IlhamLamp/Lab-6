from data import mahasiswa

#menghapus daftar mahasiswa
def hapus():
    nama = input("Masukkan nama untuk menghapus : ")
    if nama in mahasiswa.keys():
        del mahasiswa[nama]
        print("-> Daftar Mahasiswa {} telah di hapus".format(nama))
    else:
        print("-> Mahasiswa {} tidak ditemukan".format(nama))
