# Smart Edu Projesi

## Proje Hakkında

Smart Edu, Python ve Django kullanılarak geliştirilmiş bir eğitim yönetim projesidir. Projede TemplateView, fonksiyon view, url'de id'ye göre proje getirme, çoklu ve tekli ilişkiler, kullanıcı girişi ve çıkışı, kursa kayıt ve kayıttan çıkma işlemleri gibi temel Django konseptleri kullanılmıştır.

## Kullanılan Yapılar ve Teknolojiler

- **TemplateView:** Sayfa görüntüleme işlemleri için TemplateView kullanılmıştır.
- **Fonksiyon View:** Django fonksiyon view'ları, sayfa işlemlerini yönetmek için kullanılmıştır.
- **URL Parametreleri ile Çalışma:** URL'den alınan id'ye göre proje detaylarını getirme işlemleri uygulanmıştır.
- **Çoklu ve Tekli İlişkiler:** Django ORM kullanılarak kurslara etiket ve kategori atama işlemleri yapılmıştır.
- **Giriş ve Çıkış İşlemleri:** Django'nun built-in kullanıcı girişi ve çıkışı kullanılarak kullanıcı yönetimi sağlanmıştır.
- **Kursa Kayıt ve Kayıttan Çıkma İşlemleri:** Kullanıcıların kurslara kayıt olma ve kayıtlarını iptal etme işlemleri uygulanmıştır.
- **Form View:** Django'nun form view'ları, form işlemleri için kullanılmıştır.

## Projeyi Çalıştırma

1. Projeyi bilgisayarınıza klonlayın.
    ```bash
   git clone https://github.com/kullaniciadi/SmartEdu.git
2. Virtual environment oluşturun ve etkinleştirin.
    ```bash
    python -m venv venv
    Windows için: venv\Scripts\activate
3. Gerekli paketleri yükleyin.
    ```bash
    pip install -r requirements.txt
4. Veritabanını oluşturun ve uygulamayı başlatın.
    ```bash
    python manage.py migrate
    python manage.py runserver
5. ```bash 
    Tarayıcıda http://127.0.0.1:8000/ adresine giderek projeyi görüntüleyin.