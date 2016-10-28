# -*- coding:utf8 -*-
from core import *

#----------------------------------------------------------------------------------------
#新加一个Linux账户
def add_account(server, port, username, password, account, passwd):
	cmd_user = "useradd %s" % account
	cmd_pass = "echo \"%s:%s\" | /usr/sbin/chpasswd" % (account, passwd)
	check = "cat /etc/passwd | grep %s" % account
	cmds = []
	cmds.append(cmd_user)
	cmds.append(cmd_pass)
	cmds.append(check)

	ret = execute(server, port, username, password, cmds)
	return ret

#----------------------------------------------------------------------------------------
#删除Linux账户
def del_account(server, port, username, password, account):
	cmd = "userdel -f %s" % account
	cmds = []
	cmds.append(cmd)

	ret = execute(server, port, username, password, cmds)
	return ret

#----------------------------------------------------------------------------------------
#修改密码
def modify_pass(server, port, username, password, account, newpasswd):
	cmd_newpass = "echo \"%s:%s\" | /usr/sbin/chpasswd" % (account, newpasswd)
	cmds = []
	cmds.append(cmd_newpass)
	ret = execute(server, port, username, password, cmds)
	return ret