# -*- coding:utf8 -*-
from core import *

#----------------------------------------------------------------------------------------
#安装基础软件
def install_basic(server, port, username, password, ostype):
	if ostype == "centos":
		cmd_install = "yum -y install unzip ntp rsync lrzsz libaio1 python-setuptools; easy_install supervisord"
	elif ostype == "ubuntu" :
		 cmd_install = "apt-get -y install unzip ntp libaio1 rsync lrzsz snmpd python-setuptools python-pip; pip install supervisord "
	else:
		cmd_install = "uptime"

	cmds = []
	cmds.append(cmd_install)

	ret = execute(server, port, username, password, cmds)
	return ret

#----------------------------------------------------------------------------------------
#设置主机名
def set_hostname(server, port, username, password, hostname):
	genconfigfile("/tmp/hostname", "basic/hostname.tpl", {'hostname' : hostname})
	return upload(server, port, username, password, "/tmp/hostname", "/etc/hostname")

#----------------------------------------------------------------------------------------
#配置ntp
def set_ntpserver(server, port, username, password, ntpserver):
	genconfigfile("/tmp/ntp.conf", "basic/ntp.tpl", {'ntpserver' : ntpserver})
	return upload(server, port, username, password, "/tmp/ntp.conf", "/etc/ntp.conf")

#----------------------------------------------------------------------------------------
#设置history的记录格式及记录条数
def set_history(server, port, username, password):
	genconfigfile("/tmp/profile", "basic/profile.tpl")
	return upload(server, port, username, password, "/tmp/profile", "/etc/profile")
	#genconfigfile("/root/.bashrc", "basic/.bashrc.tpl")
	#upload(server, port, username, password, "/tmp/.bashrc", "/root/.bashrc")

#----------------------------------------------------------------------------------------
#设置DNS服务器
def set_nameserver(server, port, username, password):
	genconfigfile("/tmp/resolv.conf", "basic/resolv.tpl")
	return upload(server, port, username, password, "/tmp/resolv.conf", "/etc/resolv.conf")

#----------------------------------------------------------------------------------------
#设置时区
def set_timezone(server, port, username, password):
	genconfigfile("/tmp/localtime", "basic/Shanghai")
	return upload(server, port, username, password, "/tmp/localtime", "/etc/localtime")

#----------------------------------------------------------------------------------------
#关闭selinux
def set_selinux(server, port, username, password, ostype):
	if ostype == "centos":
		genconfigfile("/tmp/selinux_config", "basic/selinux.tpl")
		return upload(server, port, username, password, "/tmp/selinux_config", "/etc/selinux/config")
	else:
		return u'Other os type'

#----------------------------------------------------------------------------------------
#配置sysctl
def set_sysctl(server, port, username, password):
	genconfigfile("/tmp/sysctl.conf", "basic/sysctl.tpl")
	return upload(server, port, username, password, "/tmp/sysctl.conf", "/etc/sysctl.conf")

#----------------------------------------------------------------------------------------
#设置limlits
def set_limlits(server, port, username, password):
	genconfigfile("/tmp/security_limits.conf", "basic/limits.tpl")
	return upload(server, port, username, password, "/tmp/security_limits.conf", "/etc/security/limits.conf")
