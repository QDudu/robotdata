# robotdata
1. Python2.7-win32导入binary版本的naoqi SDKs包，即可用ALProxy对象可以在choregraphe外部连接虚拟机器人并实现机器人动作编程    
2. 如果用choregraphe则可以在项目中添加python box自动给出类的定义，需要添加onstart和onstopped函数进行动作定义；或者和给出的box库中已有的动作组合  
以上两种办法是分开的，都可独立完成驱动nao，但choregraphe可视化更直观  
  
获取机器人动作数据需要在本地安装webots,choregraphe,配置naoqi环境(python)
## webots
为能与choregraphe连接，应选择webots版本8.x,安装Webots-8.6.2
安装后打开登入：随便填一个电子邮箱，密码是:webots
(修改语言)登入后：Tools→Preferences→Chinese
打开虚拟nao机器人：Files->Open Sample World->robots->aldebaran->nao.wbt
## choregraphy
对应版本：choregraphe-suite-2.1.4.13-win32-setup
使用固定端口9559 或 固定IP：127.0.0.1 连接webots中的nao机器人
注意：本地User后的用户名不能有中文，不然无法连接虚拟机器人
