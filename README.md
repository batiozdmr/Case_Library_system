# Kütüphane Kitap Kayıt Sistemi

![Kütüphane Kitap Kayıt Sistemi](https://r.resimlink.com/ZC6bWLxFGkf.png)

Kütüphane Kitap Kayıt Sistemi, kitapların etkili bir şekilde yönetilmesi ve takip edilmesi için tasarlanmış modern ve kullanıcı dostu bir web uygulamasıdır. Bu sistem sayesinde kütüphane çalışanları, kitapların kaydedilmesi, düzenlenmesi, aranması ve ödünç verilmesi gibi işlemleri kolayca gerçekleştirebilirler.

## Özellikler

- **Kitap Kaydı:** Yeni kitapların adı, yazarı, yayın tarihi, görseli gibi bilgileri kaydedebilirsiniz.

## Nasıl Kullanılır

1. Sisteme giriş yapın veya yeni bir hesap oluşturun.
2. Yeni kitapları "Kitap Ekle" seçeneğiyle sisteme kaydedin.
3. Kitapları listeleyin.

## Teknolojiler

- **Backend:** Python ve Django kullanılarak geliştirilmiştir.
- **Frontend:** HTML, CSS ve JavaScript ile oluşturulmuştur.
- **Veritabanı:** SQLlite3 veritabanı kullanılmıştır.
- Docker Compose

### Kurulum

1. Proje dizininde, aşağıdaki komutu kullanarak sanal ortamınızı oluşturun:
```
python -m venv venv
```

2. Sanal ortamınızı etkinleştirin:

  - Windows için:
  
    ```
    venv\Scripts\activate
    ```
  
  - Linux veya macOS için:
  
    ```
    source venv/bin/activate
    ```

3. Gerekli Python paketlerini yüklemek için aşağıdaki komutu kullanın:
   pip install -r requirements.txt


4. Docker kullanarak bağımlılıkları başlatın:
   
```
docker-compose up -d
```

6. Veritabanını oluşturun:
   
```
python manage.py migrate
```

7. Geliştirme sunucusunu başlatın:
```
python manage.py runserver
```

8. Tarayıcınızda `http://localhost:8000` adresine giderek uygulamayı görüntüleyebilirsiniz.

## Katkıda Bulunma

Eğer projeye katkıda bulunmak istiyorsanız, adımları ve kuralları belirtin.

1. Bu depoyu çatallayın (fork).
2. Yeni bir özellik dalı oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi yapın, ardından bu değişiklikleri taahhüt edin (commit).
4. Dalınıza itme yapın (`git push origin yeni-ozellik`)
5. Bir Birleştirme İsteği (Pull Request) oluşturun.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. [Lisans Dosyası](LICENSE).


