# Temel imajı alın (örneğin, Python 3.8)
FROM python:3.8

# Çalışma dizinini ayarlayın
WORKDIR /app

# Gerekli kütüphaneleri kopyalayın
COPY requirements.txt requirements.txt

# Kütüphaneleri yükleyin
RUN pip install -r requirements.txt

# Proje dosyalarını kopyalayın
COPY . .

# Gerektiğinde veritabanını başlatın (örneğin, migration)
RUN python manage.py makemigrations
RUN python manage.py migrate

# Uygulamayı çalıştırın
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
