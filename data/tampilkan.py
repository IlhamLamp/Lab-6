from data import mahasiswa

#menampilkan daftar mahasiswa
def tampilkan():
    print("Daftar Nilai:")
    print("===========================================================================")
    print("| No |         Nama         |     NIM     | Tugas |  UTS  |  UAS  | Akhir |")
    print("===========================================================================")
    no = 1
    if len(mahasiswa.values()) > 0:
        for item in mahasiswa.values():
            print("| {0:2} | {1:20} | {2:11} | {3:5} | {4:5} | {5:5} | {6:5.2f} |".format
                 (no, item[0],
                  item[1], item[2],
                  item[3], item[4],
                  item[5]
                 ))
            no += 1
        print('---------------------------------------------------------------------------')
    else:
        print("|",'{:^71}'.format("TIDAK ADA DATA"),"|")
        print("===========================================================================")
