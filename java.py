# -*- coding:utf8 -*-
from core import *

#----------------------------------------------------------------------------------------
#Java安装
def Install_Java(server, port, username, password, start_area, end_area):
	global softs_path
	cmds = []
	cmd = "mkdir -p /data/kuen_ops"
	cmds.append(cmd)
	cmd = "mkdir -p /usr/local/services"
	cmds.append(cmd)
	print execute(server, port, username, password, cmds)

	localfile = softs_path + "/jdk-7u40-linux-x64.gz"
	remotefile = "/data/kuen_ops/jdk-7u40-linux-x64.gz"	#create it 
	print localfile, remotefile
	print upload(server, port, username, password, localfile, remotefile)

	cmd_tar = "tar -xvf /data/kuen_ops/jdk-7u40-linux-x64.gz -C /usr/local/services | tail -n 10"
	cmds = []
	cmds.append(cmd_tar)
	print execute(server, port, username, password, cmds)

	#上传JAVA的环境变量文件
	genconfigfile("/tmp/profile", "basic/profile.tpl")
	return upload(server, port, username, password, "/tmp/profile", "/etc/profile")