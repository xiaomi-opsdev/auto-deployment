# -*- coding:utf8 -*-
import os
import sys
import paramiko

from tornado import template
from config import *

#----------------------------------------------------------------------------------------
#远程执行命令
def execute(server, port, username, password, commands):
	ret_value = []
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server, port, username, password)
	for cmd in commands:
		stdin, stdout, stderr = ssh.exec_command(cmd)
		exit_code = stdout.channel.recv_exit_status()
		ret_value.append((exit_code, stderr.readlines(), stdout.readlines()))
	ssh.close()
	return ret_value

#----------------------------------------------------------------------------------------
#上传文件
def upload(server, port, username, password, localfile, remotefile):
	t = paramiko.Transport((server, port))
	t.connect(username = username, password = password)
	sftp = paramiko.SFTPClient.from_transport(t)
	remotepath = remotefile
	localpath = localfile
	ret = sftp.put(localpath, remotepath)
	t.close()
	return ret


#----------------------------------------------------------------------------------------
#下载文件
def download(server, port, username, password, remotefile, localfile):
	t = paramiko.Transport((server, port))
	t.connect(username = username, password = password)
	sftp = paramiko.SFTPClient.from_transport(t)
	remotepath = remotefile
	localpath = localfile
	ret = sftp.get(remotepath, localpath)
	t.close()
	return ret

#----------------------------------------------------------------------------------------
#根据模板生成配置文件(字符串)
def genconfigstring(configtemplate, configvalues = {}):
	global template_path
	loader = template.Loader(template_path)
	ret = loader.load(configtemplate).generate(**configvalues)
	print ret
	return ret

#----------------------------------------------------------------------------------------
#根据模板生成配置文件(文本文件)
def genconfigfile(configfile, configtemplate, configvalues = {}):
	fp_config = open(configfile, 'w')
	configstring = genconfigstring(configtemplate, configvalues)
	fp_config.write(configstring )
	fp_config.close()
	return configstring





