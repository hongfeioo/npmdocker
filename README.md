NodePingManageDocker
---------------------

描述
------------
本项目是NodePingManage的Docker化版本， 如果你没有python环境，但是熟悉docker，用这个吧。



服务器环境
------------
centos7


docker环境
-------------------
```bash
cat <<EOF > /etc/yum.repos.d/docker.repo
[dockerrepo]
name=Docker Repository
baseurl=https://yum.dockerproject.org/repo/experimental/centos/7/
enabled=1
gpgcheck=1
gpgkey=https://yum.dockerproject.org/gpg
EOF

yum install -y docker 

systemctl start docker; systemctl enable docker

```

启动方法
----------------
```bash
cd /home
git clone  https://github.com/hongfeioo/npmdocker.git
./buid.sh
```


配置文件格式
```bash
vi  NodePingManage/npm.ini
```
-----------------------
| 设备IP | 设备描述|初始状态关键字|邮箱|手机号|
|-----|------|----|----|----|
|114.114.114.114|CoreSwExample|Init|yihf@liepin.com|13521161889
|192.168.1.1|Server1|Init|yihf@liepin.com|13521161889


监测频率设置
---------
```bash
vi build.sh

Interval=60    指的是60s扫描一次
```



邮件短信报警模块配置
---------------------------
```bash
vi  NodePingManage/messagemodule/messageMode.py
```
[messagemodule](https://github.com/hongfeioo/messagemodule)</p>



Up,Down 报警状态机
--------------
>  5次ping测试中，有一次通则为：Up </p>
>  5次ping测试中，全部超时则为：Down , 每次ping超时时间为2秒</p>
>  检测次数和超时时间在ping.py中verbose_ping函数参数中修改 </p>



小技巧
-----------
1.   主程序中  sms_off 默认为0 ，如果为1则全局关闭短信。  </p>
2.   主程序中  mail_off 默认为 0 ，如果为1则全局关闭邮件发送。  </p>
3.   主程序中  MAX_process 默认为300， 用于限制ping的并发数。  </p>
4.   手机号或者邮箱中如果出现null字符串则跳过这个联系人. </p>
5.   当接受报警的是多邮箱或者多手机号时用分号隔开即可. </p>
6.   当你要部署多套npm的时候，npm_title 变量用来区分报警是从哪个节点产生的。</p>

程序原理介绍
---------
1.  主程序第一次运行时，从配置文件npm.ini中读取每行信息，并发对每一行的主机ip进行ping测试, 探测的结果会写入npm.tmp文件.</p>
2.  当程序第二次运行时，会先读取npm.tmp文件中数据作为参考，然后进行第二次ping探测，如果发现本次探测结果和参考状态不符，则说明状态有变化，触发报警,并把最新状态存入npm.tmp。</p>
3.  如果npm.ini进行了调整，需要删除npm.tmp文件。

排错 
------
1.   配置文件末尾请不要留空行.</p>
2.   所有日志默认输出的位置是：mylog.txt  </p>
3.   如果修改了pingModule中的文件，需要删除*.pyc  </p>
4.   如果发送邮件显示成功，但是无法收到，请检查收件箱的垃圾邮件。
5.   npm.py 修改后需要重启容器，才能生效: docker restart xxxxxx


docker的一些命令
---------
1. docker save -o python27.tar 68caceba17ab   导出一个docker镜像   
2. docker load <  python27.tar      导入镜像
3. docker tag 68caceba17ab  python:2.7  重命名镜像


作者介绍
----------
yihongfei  QQ:413999317   MAIL:yihf@liepin.com

CCIE 38649


寄语
------
麻雀虽小五脏俱全，为网络自动化运维尽绵薄之力 </p>



