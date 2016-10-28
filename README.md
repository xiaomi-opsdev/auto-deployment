#Auto_Install_console

Auto_install_console是一款小米游戏运维开发的基于SSH的自动化部署工具，只需一个有root权限的ssh账户即可完成指定业务模块的安装、配置、部署任务。
此次发布的版本为命令行版本（还有将部署任务放在消息队列中的WEB版）

模块说明：

```shell

root@ubuntu:/data/optools/Auto_install# tree
.
├── account.py          （账户管理模块）
├── Auto_Install.py     （主程序）
├── config.py           （配置文件）
├── core.py             （底层核心功能）
├── init.py             （操作系统初始化）
├── iptables.py         （iptables设置）
├── java.py             （安装JAVA环境）
├── mysql.py            （安装mysql，多实例方式）
├── redis.py            （安装redis，参数化，支持一台服务器装多个）
├── softs               （软件目录）
│   ├── jdk-7u40-linux-x64.gz
│   ├── mysql-5.5.34-linux2.6-x86_64.tar.gz
│   └── redis-2.6.16.tar.gz
└── templates           （配置文件模板）
    ├── basic
    │   ├── hostname.tpl
    │   ├── iptables
    │   │   └── iptables.tpl
    │   ├── limits.tpl
    │   ├── my.tpl
    │   ├── ntp.tpl
    │   ├── profile.tpl
    │   ├── redis.tpl
    │   ├── resolv.tpl
    │   ├── selinux.tpl
    │   ├── Shanghai
    │   ├── snmpd.tpl
    │   └── sysctl.tpl
    └── nginx
        └── nginx.template
        
```
