# Easy Time Clock
Time Clock untuk absensi jam kedatangan pegawai.

## Pre-requirement :
** For running Cassandra **
- [x] Python2.7 (for installing Cassandra)
- [x] Apache Cassandra
      For windows user can see https://youtu.be/EEXtVn3zAqc or https://medium.com/mtiakakom/praktek-instal-cassandra-di-windows-10-832bde6c3ead
-	[x] Cassandra Driver Package 
      install dengan mengetikkan ‘pip install cassandra driver’ pada CMD
      
** For running aplication script **
- [x] Python3 
- [x] tkinter or Tkinter package
- [x] time package


## Cara menjalankan script aplikasi :
1. Clone/download repository ini
2. Jalankan cassandra hingga Cassandra server (caranya bisa dilihat pada link (how to install cassandra) sebelumnya diatas). Biarkan terus berjalan.
3. Klik kanan pada file 'MyWeb.pyw', kemudian open with IDLE (Python GUI)
4. Run module
5. Setelah dirun, akan muncul tampilan login, masukkan username "dhimas" dan password "123456"
6. Klik Login as manager

## Fitur aplikasi :
**Manager**
- Login dengan menggunakan username dan password sesuai Manager masing-masing.
- Melihat Manager page yang berisi home, schedule, myEmployee, dan report.
  - Home berisi summary general dari waktu ClockIn/Out.
  - Schedule bertujuan untuk mengatur waktu ClockIn/Out.
  - MyEmployee untuk melihat list employee manager tersebut, serta bisa menambahkan employee.
  - Report untuk melihat catatan employee.
- Pada tab Home terdapat tombol "Start Time Clock untuk memulai time Clock

**Employee**
-	Cannot log in.
-	Hanya bisa input ID pada time clock untuk absensi.


## Video menjalankan aplikasi :
https://youtu.be/lxOW5pYase8
