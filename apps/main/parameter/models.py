from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext as _

from ...common.mixins.audit import AuditMixin
from ...common.fileUpload.userPath import userDirectoryPath


class SiteSettings(AuditMixin):
    site = models.OneToOneField(Site, related_name="settings", on_delete=models.CASCADE, verbose_name='Site')
    text = models.CharField(max_length=400, verbose_name=_('Site Adı'), blank=True)
    logo = models.ImageField(upload_to=userDirectoryPath, null=True, verbose_name=_('Logo'), blank=True)
    favicon = models.ImageField(upload_to=userDirectoryPath, null=True, verbose_name=_('Favicon'), blank=True)

    @property
    def logo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url

    @property
    def favicon_url(self):
        if self.favicon and hasattr(self.favicon, 'url'):
            return self.favicon.url

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = 'Site Ayarları'
        verbose_name_plural = 'Site Ayarları'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))


class Menu(AuditMixin):
    name = models.CharField(max_length=250, verbose_name='Başlık')
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name="Link")
    alignment = models.IntegerField(null=True, blank=True, verbose_name='Sıralama')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Menü'
        verbose_name_plural = 'Menü'
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi')))
