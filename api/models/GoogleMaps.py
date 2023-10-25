from django.db import models


class GoogleMaps(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    raiting = models.CharField(max_length=100, blank=True, null=True)
    count_comments = models.CharField(max_length=100, blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    recommend = models.CharField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return self.client.name
    def get_absolute_url(self):
        return f'{self.client.slug_name}/google'
    class Meta:
        db_table = 'google'
        verbose_name = 'GoogleMaps'
        verbose_name_plural = 'GoogleMaps'