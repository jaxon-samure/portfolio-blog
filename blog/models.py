from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length=100)
    contend = models.TextField()
    data_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


