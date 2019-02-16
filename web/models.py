from django.db import models

# Create your models here.

#创建分组
# class Usergroup(models.Model):
#     uid = models.AutoField(primary_key=True)
#     caption = models.CharField(max_length=64,null=True)
#     ctime = models.DateField(auto_now_add=True,null=True)
#     uptime = models.DateField(auto_now=True,null=True)
# #继承写法固定，
# #创建2个字段，分别保护姓名和密码
# class UserInfo(models.Model):
#     user = models.CharField(max_length=32)
#     pwd = models.FileField(max_length=32)
#     email = models.CharField(max_length=60)
#     test = models.EmailField(max_length=20,null=True,error_messages={'invalid':'shurumima'})
#     #创建关联
#     user_group = models.ForeignKey('Usergroup',to_field='uid',default=1)
#     user_type_choices = (
#         (1,'superuser'),
#         (2,'commounuser'),
#         (3,'com-commonuser')
#     )
#     user_type_id = models.IntegerField(choices=user_type_choices,default=1)


# class payMx(models.Model):
#     jine = models.IntegerField()
#     create_time =  models.DateTimeField()
#     end_time = models.DateTimeField()

class Usergroup(models.Model):
    uid=models.AutoField(primary_key=True)
    caption=models.CharField(max_length=62,null=True)
    ctime=models.DateField(auto_now_add=True,null=True)
    uptime=models.DateField(auto_now=True,null=True)
class Userinfo(models.Model):
    username=models.CharField(max_length=32,blank=True)
    password=models.FileField(max_length=60,help_text='pwd')
    email=models.CharField(max_length=60)
    test=models.EmailField(max_length=20,null=True,error_messages={'invalid':'shurumima'})
    user_group=models.ForeignKey('Usergroup',to_field='uid',default=1,on_delete=models.CASCADE)    #这里与上面的Usergroup表的uid进行关联，默认取到uid=1的行）
    user_type_choices=(
        (1,'superuser'),
        (2,'commonuser'),
        (3,'com-commonuser'),
    )
    user_type_id=models.IntegerField(choices=user_type_choices,default=1)