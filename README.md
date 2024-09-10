link aplikasi pws: http://agus-tini31-thriftclick.pbp.cs.ui.ac.id/

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial) ##
1) Membuat sebuah proyek Django baru
    - Membuat direktori lokal baru dengan nama thrift-click lalu menjalankan virtual environment di dalamnya.
    - Membuat berkas requirements.txt berisikan dependencies dan menginstallnya. Setelah itu, menjalankan perintah 'django-admin startproject thrift-click .' yang akan membuat folder thrift-click berisi konfigurasi dasar untuk projek Django.
    - Menambahkan localhost ke dalam ALLOWED_HOSTS lalu menjalankan server Django pada direktori lokal.
    - Membuat repositori GitHub thrift-click. Setelah itu, menginisiasi direktori lokal thrift-click sebagai repositori Git.
    - Menambahkan file .gitignore ke dalam repositori lokal lalu mempush semua perubahan pada repositori lokal ke repositori github.
2) Membuat aplikasi dengan nama main pada proyek tersebut
    - Membuat aplikasi baru dengan nama main dalam direktori proyek thrift-click dengan menjalankan perintah 'python manage.py startapp main' yang akan membuat membuat folder main yang berisi berkas-berkas dasar untuk aplikasi Django seperti views.py, models.py, dan urls.py.
    - Membuka settings.py di folder proyek, lalu tambahkan 'main' ke dalam daftar INSTALLED_APP agar Django mengenali aplikasi baru.
3) Melakukan routing pada proyek agar dapat menjalankan aplikasi main
    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    - ⁠Mengimpor fungsi include dari django.urls.
    - ⁠Menambahkan rute URL path('', include('main.urls')) untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.
4) Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut. name, price, description
    - Mengisi berkas model.py dalam aplikasi main dengan model dengan atribut atau field yang memiliki tipe data masing-masing. Untuk name, tipe datanya adalah CharField, untuk price, tipe datanya, IntegerField. Untuk description, tipe datanya TextField.
5) Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    - Membuka berkas views.py yang terletak di dalam berkas aplikasi main.
    - ⁠Mengimport render dari django.shortcuts. Menambahkan fungsi show_main yang berisi context.
    - ⁠Memasukan return render(request, "main.html", context) yang berguna untuk me-render tampilan main.html dengan menggunakan fungsi render
    - ⁠Membuka berkas main.html dan mengubah nama dan kelas menjadi struktur kode Django yang sesuai untuk menampilkan data (template variables)
6) Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    - ⁠Untuk membuat routing pada urls.py di aplikasi Django, perlu memetakan URL ke fungsi di views.py menggunakan fungsi path(). Misalnya, path('',views.home, name='home') memetakan URL root ke fungsi home di views.py, sehingga saat URL tersebut diakses, fungsi yang sesuai akan dijalankan.
7) Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat
    - Membuat new project di PWS kemudian menambahkan URL deployment "agus-tini31-thriftclick.pbp.cs.ui.ac.id" pada ALLOWED_HOST dalam settings.py sesuai username dan nama proyek di repositori lokal.
    - Menjalankan Project Command pada halaman PWS lalu mengubah nama branch menjadi main.
    - Mempush perubahan pada repositori lokal ke PWS dengan menjalankan perintah 'git push pws main:master'.
8) Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
    - Buatlah file baru dengan nama README.md di direktori utama proyek.
    - ⁠Mengedit file README.md untuk keterangan dan sesuai kebutuhan

step akhir:
- mempush semua perubahan pada repositori lokal ke repository github dan PWS
- men-deactivate virtual environment

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html ##
link bagan: 


## Jelaskan fungsi git dalam pengembangan perangkat lunak!##
Git adalah sistem kontrol versi yang membantu developer melacak perubahan kode sumber, berkolaborasi, dan mengelola versi proyek selama pengembangan perangkat lunak. Beberapa fungsi git diantaranya:
1) menyimpan versi berbeda dari sebuah proyek sebagai "commit" yang dapat mengurangi resiko kehilangan pekerjaan.
2) memungkinkan developer bekerja pada proyek yang sama secara bersamaan di mesin lokal mereka tanpa saling mengganggu pekerjaan masing-masing.
3) branching yang memungkinkan pengembang untuk membuat cabang (branch) terpisah dari proyek utama dan merging untuk (merge) menggabungkan kembali cabang tersebut ke cabang utama tanpa konflik.
4) menyediakan catatan lengkap dari siapa yang mengubah apa, kapan, dan mengapa, melalui fitur commit dan log.
5) mendeteksi konflik ketika dua pengembang melakukan perubahan pada bagian kode yang sama dan meminta pengembang untuk menyelesaikannya

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? ##
1) Django menyediakan hampir semua komponen yang diperlukan untuk membangun aplikasi web langsung dari frameworknya termasuk sistem autentikasi, ORM (Object-Relational Mapping), manajemen URL, dan formulir.
2) MVT (Model-View-Template) yang memisahkan logika bisnis, tampilan, dan kontrol, memudahkan pemula memahami alur aplikasi.
3) ORM (Object-Relational Mapping) Django memungkinkan interaksi dengan database tanpa perlu menulis SQL manual.
4) Django melindungi dari berbagai ancaman keamanan seperti CSRF (Cross-Site Request Forgery), XSS (Cross-Site Scripting), SQL Injection, dan clickjacking secara otomatis.
5) Django mendukung pengembangan aplikasi dengan cepat melalui fitur-fitur siap pakai.
6) Skalabilitas, banyak aplikasi berskala besar seperti Instagram dan Pinterest menggunakan Django, memberikan relevansi dalam dunia nyata.
7) Django adalah framework full-stack, yang berarti pengembang dapat mempelajari baik bagian front-end maupun bagian back-end.
8) Deployment yang praktis, manajemen migrasi basis data dan pengaturan konfigurasi Django mendukung proses deployment mempermudah proses deployment ke server produksi.

## Mengapa model pada Django disebut sebagai ORM? ##
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan pendekatan ORM untuk menghubungkan objek-objek Python (seperti model) dengan tabel-tabel dalam basis data relasional. ORM memungkinkan developer untuk berinteraksi dengan basis data tanpa harus menulis query SQL secara langsung. Contoh sederhana model dalam Django:
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField() 