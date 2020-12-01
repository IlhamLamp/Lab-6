from data import mahasiswa

#menambah daftar mehasiswa
def tambah():
    print("Masukkan data mahasiswa . . .")
    nama   = input("Masukkan nama : ")
    nim    = input("Masukkan nim  : ")
    n_tugas= input("Masukkan nilai tugas : ")
    n_uts  = input("Masukkan nilai uts   : ")
    n_uas  = input("Masukkan nilai uas   : ")
    n_akhir= int(n_tugas)*30/100 + int(n_uts)*35/100 + int(n_uas)*35/100

    mahasiswa[nama] = [nama, nim, n_tugas, n_uts, n_uas, n_akhir]
    print("-> Data berhasil di tambah!")
