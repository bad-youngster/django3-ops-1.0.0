from django.db import models

# Create your models here.


class UserAuth(models.Model):
    username = models.CharField(verbose_name=("用户名"), max_length=50)
    passwd = models.CharField(
        verbose_name=("密码"),
        max_length=50,
    )
    type = models.ForeignKey("UserType",
                             verbose_name=("类型,1代表普通，0代表特权用户"),
                             on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_auth'

    def __str__(self) -> str:
        return self.username


class UserType(models.Model):
    type = models.CharField(verbose_name=("类型,1代表普通，0代表特权用户"), max_length=50)

    class Meta:
        db_table = 'user_type'

    def __str__(self) -> str:
        return self.type


class MysqlInstallHistory(models.Model):
    pass


class Assets(models.Model):
    hostname = models.CharField(verbose_name=("主机名"), max_length=50)
    hostip = models.CharField(verbose_name=("主机IP"), max_length=50)
    port = models.CharField(verbose_name=("端口号"), max_length=50)

    class Meta:
        db_table = 'assets'

    def __str__(self) -> str:
        return self.hostname