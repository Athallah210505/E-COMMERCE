TUGAS 2

1.Pada checklist memberikan saya guide untuk membuat sebuah website mulai dari awal sampai deployment 
- pertama saya membuat project django baru dengan mendownload seluruh property yang diperlukan dan menggunakan virutal enviroment
- Pada directory yang sama, saya membuat file txt baru yang berisi daftar dependencies yang akan diinstall(Hal ini dilakukan agar dapat mengautomatisasi penginstallan semua dependencies yang harus diinstall)
- lalu saya menjalankan pip install -r requirements.txt untuk menginstall semua dependencies yang terdaftar di requirements.txt
- Saya juga menambahkan ""localhost", "127.0.0.1" pada bagian ALLOWED_HOSTS di file settings.py
-  Saya juga membuat file ".gitignore" agar file yang tidak perlu akan diabaikan nantinya  

- selanjutnya saya membuat main page website saya dengan membuat file main dengan kerangka html
- Dalam folder jual, kita harus menambahkan path('', include('main.urls')),pada bagian url_patterns di dalam file urls.py
- setelah itu saya mengganti beberapa komponen pada views.py untuk mengubah hal hal yang mau saya adakan pada pada website saya seperti : - nama (Charfield), quantity (Integerfield), description(TextField), price (Intergerfield)
- lalu saya melakukan integrasi terhadap main saya dan saya sesuaikan dengan komponen yang sudah saya ubah pada view.py
- saya juga melakukan routing pada urls.py agar dapat terintegrasi dengan main saya
- dan yang terkahir saya melakukan commit pada github dan juga deployment website saya pada PWS
2. link untuk bangan : https://www.canva.com/design/DAGQUyJfBOE/Gn-rtXkHpZ6i-6RMrRyP3Q/edit?utm_content=DAGQUyJfBOE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
3. fungsi git:
    1. melakukan tracking jika ada perubahan kode
    2. melakukan tracking siapa saja yang melakukan perubahan pada kode
    3. memfasilitasi para programmer untuk melakukan collaboration
4. karena django sudah memiliki komunitas yang besar dan juga sudah diapaki oleh bnayak orang yang dimana dapat emmudahkan kami pelajar untuk melakukan search dan membantu kita jika kita mendapatkan bug 
5. model django disebut juga ORM (Object-Relation-Mapping) karena django menggunakan teknik ORM mengubungkan objek pada pythondengan tabel tabel dalam database relational.


TUGAS 3 

1. Data delivery adalah proses krusial dalam sebuah platform, baik  platform web, aplikasi mobile. Proses ini melibatkan pengiriman data dari satu titik ke titik lainnya, baik itu antar komponen dalam platform itu sendiri, maupun antara platform dengan sistem eksternal.
ada beberapa alasana kenapa data delivery sangat penting:
    - Interaksi Pengguna: Data delivery memungkinkan pengguna berinteraksi dengan platform.
    - Pembarui data : dapat memperbahrui data secara berkala 
    - intergarasi sistem 
    - analisis data
- Sebagai konkulis Data delivery adalah tulang punggung dari setiap platform. Tanpa data delivery, platform tidak akan dapat berfungsi dengan baik dan memberikan nilai bagi penggunanya. Oleh karena itu, pemilihan teknologi dan arsitektur data delivery yang tepat sangat penting untuk memastikan kinerja, skalabilitas, dan keamanan platform.

2. JSON dan XML adalah representasi data yang digunakan dalam pertukaran data antaraplikasi. JSON adalah format pertukaran data terbuka yang dapat dibaca baik oleh manusia maupun mesin. JSON bersifat independen dari setiap bahasa pemrograman dan merupakan output API umum dalam berbagai aplikasi. XML adalah bahasa markah yang menyediakan aturan untuk menentukan data apa pun. XML menggunakan tanda untuk membedakan antara atribut data dan data aktual. Meskipun kedua format tersebut digunakan dalam pertukaran data, JSON adalah opsi yang lebih baru, lebih fleksibel, dan lebih populer. Menurut saya  lebih baik JSON karena lebih readable dibandingkan dengan XML
sebagai penjelasan tambahan  : 
XML (eXtensible Markup Language): Merupakan bahasa markup yang digunakan untuk mendefinisikan struktur data.
JSON (JavaScript Object Notation): Adalah format pertukaran data yang ringan dan mudah dibaca.
Mengapa JSOn lebih populer ada beberapa alasan:
    - kesedrhanaan : sintaks dalam JSON lebih sederhana yang membuatnya lebih mudah dibaca dibanding XML
    - effisiensi : Ukuran File JSON umumnya lebih kecil dibandingkan file XML yang setara, sehingga waktu transfer data menjadi lebih cepat.

3. Fungsi ""is valid()"" pada django adalah untuk memvalidasi dan memastikan data yang telah diinputkan pengguna melalui formulir.
Ketika sebuah formulir dikirimkan, Django yang akan memanggil metode ini untuk memeriksa apakah semua data yang dimasukkan sudah benar dan memenuhi persyaratan validasi yang telah ditetapkan.

4. {% csrf_token %} adalah token yang berfungsi sebagai security. Token ini di-generate secara otomatis oleh Django untuk mencegah serangan berbahaya.
Kenapa PWS penting:
    - Mencegah Aksi yang Tidak Diinginkan: Dengan menambahkan csrf_token ke dalam form, Django dapat memverifikasi bahwa permintaan yang dikirimkan berasal dari halaman yang sama di mana formulir itu ditampilkan, dan bukan dari halaman lain yang disusupi oleh penyerang.
    - Meningkatkan Keamanan Aplikasi: Serangan CSRF dapat menyebabkan konsekuensi yang serius, seperti mengubah kata sandi pengguna, melakukan transaksi tanpa izin, atau bahkan menghapus data penting. Dengan menggunakan csrf_token, kita dapat melindungi aplikasi dari jenis serangan ini.
Apa yang terjadi jika tidak menambah : 
    - Jika kita tidak menambahkan csrf_token ke dalam form, maka penyerang dapat membuat formulir palsu yang terlihat persis sama dengan formulir asli, tetapi dengan action yang berbeda. 
Bagaimana Penyerang Memanfaatkan CSRF : 
    - Formulir Palsu Penyerang dapat membuat formulir palsu yang tersembunyi di dalam sebuah gambar atau iframe yang dibenamkan di halaman web yang tidak berbahaya
    - Link Jahat Penyerang dapat membuat link yang berisi permintaan POST yang sudah diformat dengan baik.

5. 
    1. Membuat forms.py di direktori main dengan isi
    from django.forms import ModelForm
    from main.models import Product
    class ProductEntryForm(ModelForm):
        class Meta:
            model = Product  #bisa jadi salah disini
            fields = ["gold_name", "price", "quantity", "description"]
    2. Menambahkan Method create_product_entry untuk menambah entri database di file views.py di direktori main
        def create_product_entry(request):
        form = ProductEntryForm(request.POST or None)
            if form.is_valid() and request.method == "POST":
                form.save()
                return redirect("main:show_main")
            context = {
                "form": form
            }
        return render(request, "create_product.html", context)
        3. Mengimplementasikan form yang tadi sudah dibuat ke dalam laman baru dengan template html yang baru create_product.html
        4. Menambahkan lokasi folder templates tersebut ke settings.py di direktori jual_emas
            ...
            'DIRS': [BASE_DIR / 'templates'],
            ...
        5. Mengimplementasikan database ke dalam page utama main.html dan juga menjadi perpanjangan dari base.html di direktori utama
        6. Menggunakan folder static untuk mengorganisir aset yang digunakan seperti gambar.
        7. Menambahkan fungsi-fungsi yang diperlukan untuk menampilkan JSON dan XML baik secara keseluruhan maupun per entri database
            def show_xml (request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


            def show_json(request):
                data= Product.objects.all()
                return HttpResponse(serializers.serialize("json", data), content_type="application/json")

            def show_xml_by_id(request, id):
                data_id = Product.objects.filter(pk=id)  # Use the id argument passed to the function
                return HttpResponse(serializers.serialize("xml", data_id), content_type="application/xml")

            def show_json_by_id(request, id):
                data_id = Product.objects.filter(pk=id)  # Use the id argument passed to the function
                return HttpResponse(serializers.serialize("json", data_id), content_type="application/json")

        8. Merouting kembali URL yang bersangkutan di file urls.py
        path('', views.show_main, name='show_main'),
        path('create_product_entry', create_product_entry, name='create_product_entry'),
        path('xml/', show_xml, name='show_xml'),
        path ('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),


!!! DOKUMENTASI !!!

JSON 
![](static/images/raster/JSON.png)
XML
![](static/images/raster/XML.png)
JSON_ID
![](static/images/raster/JSON_ID.png)
XML_ID
![](static/images/raster/XML_ID.png)



