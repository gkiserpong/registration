from django.db import models

# Create your models here.
class Wilayah(models.Model):
    nama = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'wilayah'
        verbose_name_plural = 'Wilayah'

    def __str__(self):
        return '%s' % self.nama

    def clean(self):
        self.nama = self.nama.upper()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Wilayah, self).save(*args, **kwargs)