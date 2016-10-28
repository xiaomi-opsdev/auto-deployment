[mysqld_multi]
user            =root 
#password        ='xiaomi.c0m!@#$%'
mysqld          =/usr/local/services/mysql/bin/mysqld_safe 
mysqladmin      =/usr/local/services/mysql/bin/mysqladmin

[client]
user            =root
#password        ='xiaomi.c0m!@#$%'

{% for item in config.values() %}

[{{item['mysqld_index']}}]
port            = {{item['port']}}
socket          = {{item['socket']}}
datadir         = {{item['datadir']}}
basedir         = /usr/local/services/mysql
pid-file		= {{item['pid_file']}}	
log-error		= {{item['log_error']}}


lc-messages-dir        = /usr/local/services/mysql/share/english
character-set-server=utf8
skip-external-locking
skip-name-resolve 
wait_timeout=28800
event_scheduler=1
#transaction-isolation=READ-COMMITTED
transaction-isolation=REPEATABLE-READ
#log-bin-trust-function-creators = 1
sync_binlog=0
back_log = 50
#skip-networking
max_connections = 1000
max_connect_errors = 10000
table_open_cache = 2048
max_allowed_packet = 16M
binlog_cache_size = 32M
max_heap_table_size = 256M
sort_buffer_size = 256K
join_buffer_size = 128K
thread_cache_size = 32
thread_concurrency = 8
query_cache_size = 0
query_cache_limit = 2M
ft_min_word_len = 4
default-storage-engine = InnoDB
innodb_file_per_table=1
thread_stack = 256K
tmp_table_size = 64M
log-bin = mysql-bin
binlog_format=statement
slow_query_log
#slow_query_log_file
long_query_time = 0.5
log_warnings=0
tmpdir = {{item['tmpdir']}}
server-id = {{item['server_id']}}
key_buffer_size = 256M
read_buffer_size = 1M
read_rnd_buffer_size = 2M
bulk_insert_buffer_size = 32M
myisam_sort_buffer_size = 64M
myisam_max_sort_file_size = 2G
myisam_repair_threads = 1
sql_mode=NO_UNSIGNED_SUBTRACTION
group_concat_max_len=10240
#sql-mode=STRICT_TRANS_TABLES,NO_UNSIGNED_SUBTRACTION

# *** INNODB Specific options ***

innodb_additional_mem_pool_size = 16M

innodb_buffer_pool_size = 1000M

innodb_data_file_path = ibdata1:100M:autoextend

#innodb_data_home_dir = <directory>

innodb_file_io_threads = 4

#innodb_force_recovery=1

innodb_thread_concurrency = 8

innodb_flush_log_at_trx_commit = 0

innodb_fast_shutdown=1

innodb_log_buffer_size = 8M

innodb_log_file_size = 256M

innodb_log_files_in_group = 3

#innodb_log_group_home_dir

innodb_max_dirty_pages_pct = 75


innodb_flush_method=O_DIRECT
innodb_adaptive_hash_index=1

innodb_lock_wait_timeout = 80

binlog_stmt_cache_size = 10M
innodb_buffer_pool_instances = 7
innodb_file_format = Barracuda
innodb_thread_concurrency = 33
innodb_io_capacity = 300
innodb_purge_threads = 1
#log_slave_updates=1
relay-log=mysql-relay-bin
replicate-wild-ignore-table=test.%
replicate-wild-ignore-table=mysql.%
slave-skip-errors=1032,1062
slave_net_timeout=10
{% end %}

[mysqldump]
# Do not buffer the whole result set in memory before writing it to
# # file. Required for dumping very large tables
quick

max_allowed_packet = 16M

[mysql]
no-auto-rehash
# Only allow UPDATEs and DELETEs that use keys.
#safe-updates
[myisamchk]
key_buffer_size = 512M
sort_buffer_size = 512M
read_buffer = 8M
write_buffer = 8M

[mysqlhotcopy]
interactive-timeout
[mysqld_safe]
# Increase the amount of open files allowed per process. Warning: Make
# sure you have set the global system limit high enough! The high value
# is required for a large number of opened tables
open-files-limit = 65535
