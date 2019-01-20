from django.db import models


# Create your models here.

class DemoModel(models.Model):
    asdf = models.TextField(help_text='asdf 헬텍', max_length=100)

    ttt = models.TextField(help_text='이건 헬프텍스트', max_length=50)
