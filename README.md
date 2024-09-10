1.Pada checklist memberikan saya guide untuk membuat sebuah website mulai dari awal sampai deployment
    - pertama saya membuat project django baru dengan mendownload seluruh property yang diperlukan dan menggunakan virutal enviroment
        1. Pada directory yang sama, saya membuat file txt baru yang berisi daftar dependencies yang akan diinstall(Hal ini dilakukan agar dapat mengautomatisasi penginstallan semua dependencies yang harus diinstall)
        2. Lalu saya menjalankan pip install -r requirements.txt untuk menginstall semua dependencies yang terdaftar di requirements.txt
        3. Saya juga menambahkan ""localhost", "127.0.0.1" pada bagian ALLOWED_HOSTS di file settings.py
        4. Saya juga membuat file ".gitignore" agar file yang tidak perlu akan diabaikan nantinya  

    - kedua saya membuat main page website saya dengan membuat file main dengan kerangka html
    - Dalam folder jual, kita harus menambahkan path('', include('main.urls')),pada bagian url_patterns di dalam file urls.py
    - setelah itu saya mengganti beberapa komponen pada views.py untuk mengubah hal hal yang mau saya adakan pada pada website saya seperti : - nama (Charfield), quantity (Integerfield), description(TextField), price (Intergerfield)
    - lalu saya melakukan integrasi terhadap main saya dan saya sesuaikan dengan komponen yang sudah saya ubah pada view.py
    - saya juga melakukan routing pada urls.py agar dapat terintegrasi dengan main saya
    - dan yang terkahir saya melakukan commit pada github dan juga deployment website saya pada PWS
2. <img src= "https://www.canva.com/design/DAGQUyJfBOE/uGS1ajYMCIsmf7ZaGcmdAg/view?utm_content=DAGQUyJfBOE&utm_campaign=share_your_design&utm_medium=link&utm_source=shareyourdesignpanel">
3. git berfungsi untuk :
    1. melakukan tracking jika ada perubahan kode
    2. melakukan tracking siapa saja yang melakukan perubahan pada kode
    3. memfasilitasi para programmer untuk melakukan collaboration
4. karena django sudah memiliki komunitas yang besar dan juga sudah diapaki oleh bnayak orang yang dimana dapat emmudahkan kami pelajar untuk melakukan search dan membantu kita jika kita mendapatkan bug 
5. model django disebut juga ORM (Object-Relation-Mapping) karena django menggunakan teknik ORM mengubungkan objek pada pythondengan tabel tabel dalam database relational.
