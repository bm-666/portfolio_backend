from django.db import models


class Yandex(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    raiting = models.CharField(max_length=100, blank=True, null=True)
    count_comments = models.CharField(max_length=100, blank=True, null=True)
    create = models.DateField(auto_now=True)
    recommend = models.CharField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return self.client.name

    def get_absolute_url(self):
        return f'{self.client.slug_name}/yandex'
    class Meta:
        db_table = 'yandex'