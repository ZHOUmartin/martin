from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100) #分类名

class Tag(models.Model):
    name = models.CharField(max_length=100) #标签名

class Post(models.Model):
    title = models.CharField(max_length=70) #标题
    body = models.TextField() #正文
    created_time = models.DateTimeField() #创建时间
    modified_time = models.DateTimeField() #最后一次修改时间
    excerpt = models.CharField(max_length=200,blank=True) #摘要
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #一对多关系 一个分类可以有多篇文章
    tags = models.ManyToManyField(Tag,blank=True) #多对多关系 一篇文章可以有多个标签 一个标签也可以有多篇文章
    author = models.ForeignKey(User,on_delete=models.CASCADE) #作者 User是django已经写好的用户模型 规定一篇文章只能有一个作者

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})

    def get_index_url(self):
        return reverse('blog:index')