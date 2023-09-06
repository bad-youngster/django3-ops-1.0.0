#!/bin/bash

target_directory="/data/opt/"
file_name="rocketmq-all-4.3.2-bin-release.zip"

yum install -y unzip 

if [ -e "$target_directory/$file_name" ]; then
  echo "文件 '$file_name' 存在于目录 '$target_directory'。"
else
  echo "文件 '$file_name' 不存在于目录 '$target_directory'。"
  wget --http-user=admin  --http-passwd=admin http://192.168.0.176:8081/repository/Tools/rocketmq/rocketmq-all-4.3.2-bin-release.zip
  md5sum_value=$(md5sum "$target_directory/$file_name" | awk '{print $1}')
fi

unzip $target_directory/$file_name -d $target_directory

nohup sh /data/opt/rooketmq_4.3.2/bin/mqbroker -c /data/opt/rooketmq_4.3.2/conf/broker-01-slave.properties > /data/opt/rooketmq_4.3.2/logs/broker-01-slave.log 2>&1 &
nohup sh /data/opt/rooketmq_4.3.2/bin/mqbroker -c /data/opt/rooketmq_4.3.2/conf/broker-02-master.properties > /data/opt/rooketmq_4.3.2/logs/broker-02-master.log 2>&1 &

nohup sh /data/opt/rooketmq_4.3.2/bin/mqnamesrv > /data/opt/rooketmq_4.3.2/logs/mqnameserver.log 2>&1 &