from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class UserAuth(models.Model):
    hostname = models.CharField(_("主机名"), max_length=50)
    ipadders = models.CharField(_("ip地址"), max_length=50)
    username = models.CharField(_("用户名"), max_length=50)
    passwd = models.CharField(_("密码"), max_length=50)
    port = models.CharField(_("端口号"), max_length=50)
    type = models.CharField(_("类型"), max_length=50)

    class Meta:
        db_table = 'user_auth'

    def __str__(self) -> str:
        return self.hostname
