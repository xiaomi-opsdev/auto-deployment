# -*- coding:utf8 -*-
from core import *

#----------------------------------------------------------------------------------------
#安装Redis
def Install_Redis(server, port, username, password, start_area, end_area):
	global softs_path
	#需要事先创建/data/kuen_ops/目录，否则无法上传文件
	cmds = []
	cmd = "mkdir -p /data/kuen_ops"
	cmds.append(cmd)
	cmd = "yum -y install gcc automake autoconf libtool make"
	cmds.append(cmd)
	print execute(server, port, username, password, cmds)

	#上传redis
	localfile_redis = softs_path + "/redis-2.6.16.tar.gz"
	remotefile_redis = "/data/kuen_ops/redis-2.6.16.tar.gz"
	print upload(server, port, username, password, localfile_redis, remotefile_redis)

	#redis安装过程
	cmds = []
	cmd_mkdir = "mkdir -p /data/kuen_ops/;"
	cmds.append(cmd_mkdir)
	cmd_mkdir = "mkdir -p /usr/local/services/;"
	cmds.append(cmd_mkdir)
	cmd_tar = "tar -zxvf /data/kuen_ops/redis-2.6.16.tar.gz -C /usr/local/services | tail -n 10"
	cmds.append(cmd_tar)

	#Redis编译指令
	cmd_redis = "cd /usr/local/services/redis-2.6.16/;"
	for i in xrange(0, end_area - start_area + 1):
		cmd_redis += "make PREFIX=/usr/local/services/redis%d install;mkdir -p /usr/local/services/redis%d/{var,logs,etc};" % (i, i)

	cmds.append(cmd_redis)
	print execute(server, port, username, password, cmds)
	conf_redis(server, port, username, password, start_area, end_area)

#----------------------------------------------------------------------------------------
#配置redis
def conf_redis(server, port, username, password, start_area, end_area):
	redis_config = {}
	for i in xrange(0, end_area - start_area + 1):
		redis_config['redis_root'] = r"/usr/local/services/redis%d" % i
		redis_config['port'] = 6379 + i
		#configfile = r"/usr/local/services/redis%d/etc/redis.conf" % i
		tmpconfigfile = r"/tmp/redis%d.conf" % i
		configtemplate = "basic/redis.tpl"
		configfile = r"/usr/local/services/redis%d/etc/redis.conf" % i
		print genconfigfile(tmpconfigfile, configtemplate, redis_config)
		print upload(server, port, username, password, tmpconfigfile, configfile)