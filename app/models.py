from django.db import models

# Create your models here.


class UserAuth(models.Model):
    nickname = models.CharField(verbose_name=("昵称"), max_length=50)
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
    h_id = models.CharField(verbose_name=("执行id"), max_length=50)
    h_ip = models.CharField(verbose_name=("执行主机IP"), max_length=50)
    h_user = models.CharField(verbose_name=("执行用户"), max_length=50)
    h_type = models.CharField(verbose_name=("类型"), max_length=50)
    h_d_url = models.CharField(verbose_name=("版本"), max_length=50)
    h_s_url = models.CharField(verbose_name=("脚本"), max_length=50)
    h_status = models.CharField(verbose_name=("状态"), max_length=50)

    class Meta:
        db_table = 'mysql_install_history'

    def __str__(self) -> str:
        return self.h_id


class Assets(models.Model):
    hostname = models.CharField(verbose_name=("主机名"), max_length=50)
    hostip = models.CharField(verbose_name=("主机IP"), max_length=50)
    port = models.CharField(verbose_name=("端口号"), max_length=50)

    class Meta:
        db_table = 'assets'

    def __str__(self) -> str:
        return self.hostname


class AliyunAssets(models.Model):
    regionId = models.CharField(verbose_name=("实例区域"), max_length=50)
    instanceIds = models.CharField(verbose_name=("实例id"), max_length=50)
    dataSnapshotId = models.CharField(verbose_name=("数据盘快照id"), max_length=50)
    instanceName = models.CharField(verbose_name=("实例名称"), max_length=50)
    instanceType = models.CharField(verbose_name=("实例类型"), max_length=50)
    instanceChargeType = models.CharField(verbose_name=("付费模式"), max_length=50)
    keyPairName = models.CharField(verbose_name=("密钥名称"), max_length=50)
    securityGroupId = models.CharField(verbose_name=("安全组id"), max_length=50)
    vSwitchId = models.CharField(verbose_name=("虚拟交换机"), max_length=50)

    class Meta:
        db_table = 'aliyun_assets'

    def __str__(self) -> str:
        return self.regionId


class AliyunEcsAssets(models.Model):
    regionId = models.CharField(verbose_name=("实例区域id"), max_length=50)
    instanceId = models.CharField(verbose_name=("实例id"), max_length=50)
    instanceName = models.CharField(verbose_name=("实例名称"), max_length=50)
    memory = models.CharField(verbose_name=("内存"), max_length=50)
    instanceChargeType = models.CharField(verbose_name=("付费类型"), max_length=50)
    cpu = models.CharField(verbose_name=("cpu"), max_length=50)
    osName = models.CharField(verbose_name=("系统名称"), max_length=50)
    expiredTime = models.CharField(verbose_name=("到期时间"), max_length=50)
    imageId = models.CharField(verbose_name=("镜像id"), max_length=50)
    status = models.CharField(verbose_name=("实例状态"), max_length=50)
    startTime = models.CharField(verbose_name=("开始时间"), max_length=50)
    privateIpAddress = models.CharField(verbose_name=("私有IP"), max_length=50)
    vpcId = models.CharField(verbose_name=("vpc Id"), max_length=50)
    vswitchId = models.CharField(verbose_name=("虚拟网卡"), max_length=50)
    instanceType = models.CharField(verbose_name=("实例类型"), max_length=50)
    keyPairName = models.CharField(verbose_name=("密钥对"), max_length=50)
    zoneId = models.CharField(verbose_name=("地区id"), max_length=50)
    tags = models.CharField(verbose_name=("标签"), max_length=500)
    securityGroupIds = models.CharField(verbose_name=("安全组id"), max_length=500)

    class Meta:
        db_table = 'aliyun_ecs_assets'

    def __str__(self) -> str:
        return self.regionId


class AliyunDescribeRegions(models.Model):
    regionId = models.CharField(verbose_name=("实例区域id"), max_length=50)
    regionEndpoint = models.CharField(verbose_name=("实例端点"), max_length=50)
    localName = models.CharField(verbose_name=("本地名称"), max_length=50)

    class Meta:
        db_table = 'aliyun_describe_Regions'

    def __str__(self) -> str:
        return self.regionId