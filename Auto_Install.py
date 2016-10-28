# -*- coding:utf8 -*-
#导入各模块

from core import *
from config import *
from account import *
from init import *
from iptables import *
from java import *
from mysql import *
from redis import *

#----------------------------------------------------------------------------------------
#主函数
if __name__ == "__main__":
    servers = ["10.108.96.194",
              "10.99.169.78",
              ]

    port = 22
    username = "root"
    password = "d76b29a163e4dfb"
    #需要新加的账户名及密码
    account = "xiaomi_game"
    passwd = "f09a9d6fbddb3d8f"
    #要修改成什么密码
    newpasswd = "2fd59e9a8188bdbc5"

    iptables_file = "xiaomi_firewall.sh"
    iptables_template = "basic/iptables/iptables.tpl"

    ntpserver = "210.72.145.44"  #国家授时中心服务器IP地址
    #单服务器中配置多个区时，需要指定起始的区号
    start_area 	= 1
    end_area	= 2


    #执行安装操作
    for server in servers:
        add_account(server, port, username, password, account, passwd)
        modify_pass(server, port, username, password, account, newpasswd)
        del_account(server, port, username, password, account)
        set_iptables(server, port, username, password, iptables_file, iptables_template)
        set_hostname(server, port, username, password, 'xiaomigame')
        set_ntpserver(server, port, username, password, ntpserver)
        set_history(server, port, username, password)  # profile也在里面
        set_nameserver(server, port, username, password)
        set_limlits(server, port, username, password)
        Install_Redis(server, port, username, password, start_area, end_area)
        Install_Java(server, port, username, password, start_area, end_area)
        Install_mysql(server, port, username, password, start_area, end_area)