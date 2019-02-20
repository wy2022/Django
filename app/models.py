from django.db import models

# Create your models here.
class user(models.Model):
    account = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email =models.EmailField(null=True)
    tel = models.IntegerField(null=True)
    #枚举
    user_type_choices = (
        (1,'youke'),
        (2,'huiyuan'),
        (3,'chaojiguanliyuan'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices,default=1)
    status = models.BooleanField(default=True,help_text='开启或者禁用状态')
    Text =models.TextField(null=True)
    slug = models.SlugField(null=True)
    IP = models.GenericIPAddressField(default='127.0.0.1')
    url = models.URLField(null=True)
    # file_path =models.FilePathField(path="H:/123",null=True)
    file = models.FileField(upload_to="app/123",default='/1231')#这个路径只能在项目内，如果到H:/123将会出错。
    img = models.ImageField(upload_to="app/123",default='/1231' )

    insert_time = models.DateTimeField(auto_now_add=True,null=True)
    update_time = models.DateTimeField(auto_now=True,null=True)

