# -*- coding:utf8 -*-
from core import *

#安装Mysql
#----------------------------------------------------------------------------------------
def Install_mysql(server, port, username, password, start_area, end_area):
	global softs_path
	Install_path = "/usr/local/services/mysql"		#mysql安装目录
	localfile = softs_path + "/mysql-5.5.34-linux2.6-x86_64.tar.gz"
	remotefile = "/data/kuen_ops/mysql-5.5.34-linux2.6-x86_64.tar.gz"

	cmds = []
	cmd = "yum -y install perl perl-devel libaio"
	cmds.append(cmd)
	cmd = "mkdir -p /data/kuen_ops/; mkdir -p /usr/local/services; chown -R mysql:mysql /usr/local/services/mysql"
	print execute(server, port, username, password, cmds)

	#上传mysql到目标服务器
	print upload(server, port, username, password, localfile, remotefile)
	cmd_tar = "tar -zxvf /data/kuen_ops/mysql-5.5.34-linux2.6-x86_64.tar.gz -C /usr/local/services | tail -n 10"
	cmds = []
	cmds.append(cmd_tar)
	cmd = "cp -fr /usr/local/services/mysql-5.5.34-linux2.6-x86_64 /usr/local/services/mysql;"
	cmds.append(cmd)
	cmd = "groupadd mysql;useradd -g mysql mysql;"
	cmds.append(cmd)
	cmd = "mkdir -p /var/run/mysqld/;chown -R mysql.mysql /var/run/mysqld/;mkdir -p /usr/local/services/mysql/etc;"
	cmds.append(cmd)
	print execute(server, port, username, password, cmds)

	#Mysql配置并启动
	config = {}
	cmds = []
	cmd_initdb = ""
	cmd = ""
	for x in xrange(0, end_area - start_area + 1):
		cmd += "mkdir -p /data/mysql%d /data/mysql%d/tmp;chown -R mysql.mysql /data/mysql%d/tmp;" % (x + 1, x + 1, x + 1)
		mysql_config = dict(
		mysqld_index = "mysqld%d" % (x + 1),
		port = 3306 + x,
		socket = "/tmp/mysql_%d.sock1" % (3306 + x),
		datadir = "/data/mysql%d" % (x + 1),
		tmpdir = "/data/mysql%d/tmp" % (x + 1),
		server_id = start_area + x,
		pid_file = "/var/run/mysqld/mysqld%d.pid" % (3306 + x),
		log_error = "/var/log/mysql/error%d.log" % (3306 + x)
		)
		k = "mysqld%d" % (x + 1)
		config[k] = mysql_config
		cmd_initdb = "/usr/local/services/mysql/scripts/mysql_install_db --user=mysql --basedir=/usr/local/services/mysql --datadir=/data/mysql%d --port=%d;" % (x + 1, 3306 + x)

	tmpconfigfile = "/tmp/my.cnf"
	templatefile = "basic/my.tpl"
	configfile = "/usr/local/services/mysql/etc/my.cnf"
	print genconfigfile(tmpconfigfile, templatefile, {'config' : config})
	print tmpconfigfile, configfile
	print upload(server, port, username, password, tmpconfigfile, configfile)
	print cmd_initdb
	cmd_setpath = "export PATH=$PATH:/usr/local/services/mysql/bin;"
	cmd_startdb = "mkdir /var/log/mysql;/usr/local/services/mysql/bin/mysqld_multi  --defaults-extra-file=/usr/local/services/mysql/etc/my.cnf start"
	cmds.append(cmd)
	cmds.append(cmd_initdb)
	cmds.append(cmd_setpath)
	cmds.append(cmd_startdb)
	print execute(server, port, username, password, cmds)