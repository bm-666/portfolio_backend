from django.db import models


class DoubleGis(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    raiting = models.CharField(max_length=100, blank=True, null=True)
    count_comments = models.CharField(max_length=100, blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    recommend = models.CharField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return self.client.name
    def get_absolute_url(self):
        return f'{self.client.slug_name}/double_gis'
    class Meta:
        db_table = 'double_gis'
        verbose_name = '2Gis'
        verbose_name_plural = '2Gis'