""" 
记录传感器的角度数据，并将其写入.csv表格中
"""

# MEMORY_VALUE_NAMES is the list of ALMemory values names you want to save.
ALMEMORY_KEY_NAMES = [
"Device/SubDeviceList/HeadYaw/Position/Sensor/Value",
"Device/SubDeviceList/HeadYaw/Position/Actuator/Value",
]

ROBOT_IP = "127.0.0.1"

import os
import sys
import time
from naoqi import ALProxy

def recordData(nao_ip):
    """ 
    Record the data from ALMemory.
    Returns a matrix of values
    """
    print "Recording data ..."
   
    # 用ALProxy类的ALMemory创建对象
    memory = ALProxy("ALMemory", nao_ip, 9559)
    
    data = list()
    for i in range (1, 100):
        line = list()
        for key in ALMEMORY_KEY_NAMES:
            
            # 用getData（关节名称）读数据
            value = memory.getData(key)
            line.append(value)
        data.append(line)
        time.sleep(0.05)
    return data


def main()：
    if len(sys.argv) < 2:
        nao_ip = ROBOT_IP
    else:
        nao_ip = sys.argv[1]
    motion = ALProxy("ALMotion", nao_ip, 9559)
    '''
    设置机器人头部控制器的刚度 setStiffnesses
    所有能控制的参数与函数方法具体见：http://doc.aldebaran.com/2-1/naoqi/motion/almotion.html
    '''
    motion.setStiffnesses("Head", 1.0)
    '''
    使用angleInterpolation 方法，控制机器人头部电机（ "HeadYaw" 轴）
    从1.0弧度变换到0.0弧度，变换过程在两秒内完成。
    最后一个参数 False 表示这个动作不需要等待完成，而是可以立即返回执行其他操作。
    也即非阻塞，同时进行数据的读取
    '''
    motion.post.angleInterpolation(
        ["HeadYaw"],
        [1.0, 0.0],
        [1  , 2],
        False
    )
    data = recordData(nao_ip)
    # 恢复机器人头部刚度值
    motion.setStiffnesses("Head", 0.0)

    output = os.path.abspath("record.csv")
    with open(output, "w") as fp:
        for line in data:
            fp.write("; ".join(str(x) for x in line))
            fp.write("\n")
    print "Results written to", output


if __name__ == "__main__":
    main()

