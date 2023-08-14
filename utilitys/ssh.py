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
        ssh = SSHClient()
        ssh._transport = self.connect()
        stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
        res = to_str(stdout.read())
        error = to_str(stderr.read())
        if error.strip():
            return {'code': 400, 'res': error}
        else:
            return {'code': 200, 'res': res}

    def upload(self, local_path, target_path):
        sftp = SFTPClient.from_transport(self.connect())
        sftp.put(local_path, target_path, confirm=True)
        sftp.chmod(target_path, 0o755)

    def download(self, target_path, local_path):
        sftp = SFTPClient.from_transport(self.connect())
        sftp.get(target_path, local_path)

    def __del__(self):
        self.close()
