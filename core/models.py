from django.db import models

# Create your models here.
class QuesModel(models.Model):
  id = models.AutoField(primary_key=True)
  category = models.CharField(max_length=30, null=True)
  question = models.CharField(max_length=200,null=True)
  op1 = models.CharField(max_length=200,null=True)
  op2 = models.CharField(max_length=200,null=True)
  op3 = models.CharField(max_length=200,null=True)
  ans = models.CharField(max_length=200,null=True)
  
  def __str__(self):
    ques_display = f"ID: {self.id} | Category: {self.category} | Question: {self.question}"
    return ques_display