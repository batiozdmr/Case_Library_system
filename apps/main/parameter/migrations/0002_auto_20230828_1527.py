# Generated by Django 3.2.16 on 2023-08-28 12:27

import apps.common.fileUpload.userPath
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('parameter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('name', models.CharField(max_length=250, verbose_name='Başlık')),
                ('link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Link')),
                ('alignment', models.IntegerField(blank=True, null=True, verbose_name='Sıralama')),
            ],
            options={
                'verbose_name': 'Menü',
                'verbose_name_plural': 'Menü',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(blank=True, max_length=400, verbose_name='Site Adı')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=apps.common.fileUpload.userPath.userDirectoryPath, verbose_name='Logo')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to=apps.common.fileUpload.userPath.userDirectoryPath, verbose_name='Favicon')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='sites.site', verbose_name='Site')),
            ],
            options={
                'verbose_name': 'Site Ayarları',
                'verbose_name_plural': 'Site Ayarları',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
