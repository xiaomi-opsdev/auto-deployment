# -*- coding:utf8 -*-
from core import *

#----------------------------------------------------------------------------------------
#设置iptables
def set_iptables(server, port, username, password, iptables_file, iptables_template, configvalues = {}):
	genconfigfile(iptables_file, iptables_template)
	if os.path.exists(iptables_file):
		remotefile = "/etc/%s" % iptables_file
		upload(server, port, username, password, iptables_file, remotefile)
		chmod_firewall = "chmod 755 %s" % remotefile
		cmd_firewall = "sh %s" % remotefile
		cmds = []
		cmds.append(chmod_firewall)
		cmds.append(cmd_firewall)

		ret = execute(server, port, username, password, chmod_firewall)
		return ret
	else:
		error = u"生成配置文件失败"
		return error