from django.db import models
from django.utils import timezone

class Oper(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    sum_debet = models.DecimalField(decimal_places=2, max_digits=12)
    sum_credit = models.DecimalField(decimal_places=2, max_digits=12)
    text = models.TextField()
    date = models.DateField()
    created_date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(default=timezone.now)
    #zakaz = models.CharField(max_length=10)
    #st_credit = models.CharField(max_length=20)

    def __str__(self):
        return str(self.date)+" Приход="+str(self.sum_debet)+" Расход="+str(self.sum_credit)+" Комментарий:"+self.text
