# robotdata
1. Python2.7-win32导入binary版本的naoqi SDKs包，用ALProxy对象接口，而不使用choregraphe，python编程直接连接虚拟机器人并实现机器人动作控制  
2. choregraphe可以在新建项目中：添加python box，在自动给出类的定义的基础上添加onstart和onstopped函数进行动作定义；或者用box库中已有的动作进行组合  
以上两种办法是分开的，都可独立完成驱动nao，但choregraphe可视化更直观  
  
获取机器人动作数据需要在本地安装webots,choregraphe,配置naoqi环境(python)
## webots
为能与choregraphe连接，应选择webots版本8.x,安装Webots-8.6.2  
安装后打开登入：随便填一个电子邮箱，密码是:webots  
(修改语言)登入后：Tools→Preferences→Chinese  
打开虚拟nao机器人：Files->Open Sample World->robots->aldebaran->nao.wbt  
## choregraphe
安装：choregraphe-suite-2.1.4.13-win32-setup  
使用固定端口9559 或 固定IP：127.0.0.1 连接webots中的nao机器人  
注意：本地User后的用户名不能有中文，不然无法连接虚拟机器人  
## 配置naoqi环境
安装：python-2.7.18-32位(Windows x86 MSL安装程序)
setup过程中选择将python2.7.18配置到PATH环境变量  
下载Nao机器人的SDK: pynaoqi-python2.7-2.1.4.13-win32-vs2010  
解压后将：pynaoqi-python2.7-2.1.4.13-win32-vs2010\ 添加到用户变量中  
验证：cmd->python27->import naoqi  
opencv：pip install opencv-python==4.2.0.32  

## Method 1  NAO Python API
[ALProxy](http://doc.aldebaran.com/2-1/naoqi/index.html)  
1. test.py:  
   用默认IP和端口地址实现机器人连接；定义一个控制机器人动作的ALProxy对象  
   运行test.py可检查与机器人是否连接成功(前提是Webots按上述方法安装并打开nao)  
2. info.py:  
   输出当前连接到的机器人的配置信息：类型与版本
   此安装方法对应的是机器人：naoH25  
   [body_type](	http://doc.aldebaran.com/2-1/family/body_type.html)
3. pose.py:  
   ```
   motionProxy  = ALProxy("ALMotion", robotIP, PORT)  
   postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
   ```
   控制nao的动作以及目标姿势，驱动机器人  
   [keywords](http://doc.aldebaran.com/2-1/family/nao_h25/joints_h25.html)  
   [ALRobotPosture](http://doc.aldebaran.com/2-1/naoqi/motion/alrobotposture.html#alrobotposture)  
   [ALMotion](	http://doc.aldebaran.com/2-1/naoqi/motion/almotion-api.html)
5. data_recording.py:  
   两个任务并行（非阻塞调用）：  
   a. recordData函数读取ALMemory的记录数据，读取时间间隔为0.05s   
   b. motion驱动机器人的头部转动，设定转动角度范围  
   最后将读取数据输出到.csv表格中  
   [ALMemory](http://doc.aldebaran.com/2-1/naoqi/core/almemory.html)  
## Method 2 Choregraphe+Naoqi ！！
1. 在choregraphe定义好一个项目动作后，将这一机器人程序发送至机器人  
   发送行为文件成功，在choregraphe机器人应用程序面板处可以看到当前程序下行为的名称：此例中为"behavior_1"
2. manage.py  
   调用ALBehaviorManager,控制机器人程序的动作，可以控制开始、暂停、持续时间、默认动作等  
   [APLBehaviorManager](http://doc.aldebaran.com/2-1/naoqi/core/albehaviormanager.html)  
   调用Method 1中的recordData函数，获取关节运动信息  
## Method 3 Choregraphe -> behavior
在choregraphe保存的设计好的项目文件中有behavior文件夹下的.xar或.xml文件里面包含：  
1. python动作程序  
2. 控制机器人关节动作的一系列关键帧的的帧序号以及值（弧度）  


