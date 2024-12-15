from django.db import models

class App(models.Model):
    app_name = models.CharField(max_length=255)
    version = models.CharField(max_length=20)
    description = models.TextField()
    
    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'Apps'
        
    def __str__(self):
        return self.app_name
