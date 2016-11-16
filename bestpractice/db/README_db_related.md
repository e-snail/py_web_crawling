
重置mysql密码

$ /etc/init.d/mysql stop
$ sudo  mysqld_safe --user=mysql --skip-grant-tables --skip-networking &
$ mysql -u root -p


数据库连接错误 "pymysql.connect, Errno 111] Connection refused"

use "mysqladmin variables | grep socket" to get unix_socket
更改连接参数