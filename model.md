# Model.md

Dalam mengembanggkan aplikasi ini, penulis menggunakan Python3 sebagai basis codenya, dan menggunakan Tkinter sebagai Tampilan/User Interfacenya. Selain itu penulis juga menggunakan apache-cassandra.

Segala perhitungan dan pemrosesan akan dilakukan oleh system TimeClock

Dalam perancangan ini, menggunakan 5 model:

Admin 
Tugas admin disini untuk mengatur akun-akun manager dan melihat report
disni datanya berupa ```Id_Number, Username, Password``` 

Manager 
Tugas manager disini untuk mengatur kapan Time Clock berjalan, dan mengatur Employee
disini datanya berupa ```ID_number, username, password, Name, department``` 

Employee
Berisi data tentang employee
disini datanya berupa ```ID_Number, Name, department, salaryhour, workhour, totalsalary```

Schedule
disini datanya berupa ```ID_Number, Days, Time```

Report
disini datanya berupa ```ID_Number, Content```
