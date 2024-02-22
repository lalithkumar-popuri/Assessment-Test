from django.db import models

class Proxy(models.Model):
    ip = models.CharField(max_length=100)
    port = models.IntegerField()
    protocol = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    uptime = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Proxy"
        verbose_name_plural = "Proxies"