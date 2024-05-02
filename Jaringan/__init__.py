import mysql.connector
from mysql.connector import errorcode

try:
    db_config=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='mahasiswa'
    )
    cursor=db_config.cursor()
    print("Koneksi ke Database Berhasil")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Username atau Password salah")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database tidak ditemukan")
    else:
        print(err)

def pilih_menu():
    print("____ CRUD ____")
    print("[1] Lihat Daftar Mahasiswa")
    print("[2] Tambah Mahasiswa")
    print("[3] Edit Data Mahasiswa")
    print("[4] Hapus Data Mahasiswa")
    print("_______________")
    
    pilihan=input("Pilih Menu=  ")
    if(pilihan== "1"):
        daftar_mahasiswa()
    elif(pilihan=="2"):
        tambah_mahasiswa()
    elif(pilihan=="3"):
        edit_mahasiswa()
    elif(pilihan=="4"):
        hapus_mahasiswa()
    else:
        print("Kamu memilih menu yang salah!!")

def daftar_mahasiswa():
    sql="SELECT * FROM mhs"
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        print(row)

def tambah_mahasiswa():
    print("----- Tambah Data Mahasiswa ------")
    id=input("Masukan id Mahasiswa :")
    nama=input("Masukan nama Mahasiswa : ")
    nim=input("Masukan Nim Mahasiswa : ")
    jurusan=input("Masukan Jurusan Mahasiswa : ")
    sql="INSERT INTO mhs(id,nama,nim,jurusan) VALUES (%s,%s,%s,%s)"
    val=(id,nama,nim,jurusan)
    cursor.execute(sql,val)
    db_config.commit()
    print("Data Mahasiswa Berhasil Ditambahkan")
    
def edit_mahasiswa():
    print("----- Edit Mahasiswa ------")
    id_edit=input("Masukan id mahasiswa yang akan diedit : ")
    nama=input("Masukan nama mahasiswa : ")
    nim=input("Masukan nim Mahasiswa : ")
    jurusan=input("Masukan jurusan mahasiswa : ")
    sql="UPDATE mhs SET nama=%s,nim=%s,jurusan=%s WHERE id=%s"
    val= (nama,nim,jurusan,id_edit)
    cursor.execute(sql,val)
    db_config.commit()
    print("Data mahasiswa berhasil di edit")
    
def hapus_mahasiswa():
    print("--- Hapus Data Mahasiswa ---")
    hapus_id=input("Masukan id mahasiswa yang akan dihapus :")
    sql="DELETE FROM mhs WHERE id=%s"
    value=(hapus_id)
    cursor.execute(sql,(value,))
    db_config.commit()
    print("Data mahasiswa berhasil dihapus")
    
if __name__=="__main__":
    while True:
        pilih_menu()
