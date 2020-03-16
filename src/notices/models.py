from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    about = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.about}: {self.title}'