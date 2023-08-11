# -*- coding: utf-8 -*-
# @Time  : 2023/08/08 17:02:33
# @Author: wy
from paramiko import Transport, SFTPClient
from paramiko.client import SSHClient, AutoAddPolicy
from paramiko.rsakey import RSAKey
from paramiko.auth_handler import AuthHandler
from paramiko.ssh_exception import AuthenticationException, SSHException
from utilitys.unicode_utils import to_str


class Ssh:

    def __init__(self, host_dict):
        self.host = host_dict['host']
        self.port = host_dict['port']
        self.username = host_dict['username']
        self.pwd = host_dict['pwd']
        self.__k = None

    def connect(self):
        transport = Transport((self.host, int(self.port)))
        transport.connect(username=self.username, password=self.pwd)
        return transport

    def close(self):
        self.connect().close()

    def run_cmd(self, command):
        """
         执行shell命令,返回字典
         return {'color': 'red','res':error}或
         return {'color': 'green', 'res':res}
        :param command:
        :return:
        """
        ssh = SSHClient()
        ssh._transport = self.connect()
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        res = to_str(stdout.read())
        # 获取错误信息
        error = to_str(stderr.read())
        # 如果有错误信息，返回error
        # 否则返回res
        if error.strip():
            return {'code': 400, 'res': error}
        else:
            return {'code': 200, 'res': res}

    def upload(self, local_path, target_path):
        # 连接，上传
        sftp = SFTPClient.from_transport(self.connect())
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(local_path, target_path, confirm=True)
        # print(os.stat(local_path).st_mode)
        # 增加权限
        # sftp.chmod(target_path, os.stat(local_path).st_mode)
        sftp.chmod(target_path, 0o755)  # 注意这里的权限是八进制的，八进制需要使用0o作为前缀

    def download(self, target_path, local_path):
        # 连接，下载
        sftp = SFTPClient.from_transport(self.connect())
        # 将location.py 下载至服务器 /tmp/test.py
        sftp.get(target_path, local_path)

    def __del__(self):
        self.close()
