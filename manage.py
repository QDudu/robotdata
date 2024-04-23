# -*- encoding: UTF-8 -*-
import os
import sys
import time
from data_recording import recordData
from naoqi import ALProxy

nao_ip="127.0.0.1"

def main(robotIP, behaviorName):
    # Create proxy to ALBehaviorManager
    managerProxy = ALProxy("ALBehaviorManager", robotIP, 9559)
    '''
    语句顺序为：
    先控制机器人动作程序执行
    再读取读取数据
    这样才可以在行为发生的同时记录数据
    '''
    managerProxy.startBehavior(behaviorName) #行为程序执行！！
    data = recordData(nao_ip)
    
    #getBehaviors(managerProxy)
    #launchAndStopBehavior(managerProxy, behaviorName)
    #defaultBehaviors(managerProxy, behaviorName)
    # 以上三个函数是文档里给出的实例，用来控制行为的开始，暂停，以及将行为加入默认行为列表
    # startBehavior就可以完整执行一遍整个动作

    output = os.path.abspath("record.csv")

    with open(output, "w") as fp:
        for line in data:
            fp.write("; ".join(str(x) for x in line))
            fp.write("\n")

    print "Results written to", output


def getBehaviors(managerProxy):
    ''' Know which behaviors are on the robot '''

    names = managerProxy.getInstalledBehaviors()
    print "Behaviors on the robot:"
    print names

    names = managerProxy.getRunningBehaviors()
    print "Running behaviors:"
    print names

def launchAndStopBehavior(managerProxy, behaviorName):
    ''' Launch and stop a behavior, if possible. '''

    # Check that the behavior exists.
    if (managerProxy.isBehaviorInstalled(behaviorName)):

        # Check that it is not already running.
        if (not managerProxy.isBehaviorRunning(behaviorName)):
            # Launch behavior. This is a blocking call, use post if you do not
            # want to wait for the behavior to finish.
            managerProxy.post.runBehavior(behaviorName)
            time.sleep(0.5)
        else:
            print "Behavior is already running."

    else:
        print "Behavior not found."
        return

    names = managerProxy.getRunningBehaviors()
    print "Running behaviors:"
    print names

    # Stop the behavior.
    if (managerProxy.isBehaviorRunning(behaviorName)):
        managerProxy.stopBehavior(behaviorName)
        time.sleep(1.0)
    else:
        print "Behavior is already stopped."

    names = managerProxy.getRunningBehaviors()
    print "Running behaviors:"
    print names


def defaultBehaviors(managerProxy, behaviorName):
    ''' Set a behavior as default and remove it from default behavior. '''

    # Get default behaviors.
    names = managerProxy.getDefaultBehaviors()
    print "Default behaviors:"
    print names

    # Add behavior to default.
    managerProxy.addDefaultBehavior(behaviorName)

    names = managerProxy.getDefaultBehaviors()
    print "Default behaviors:"
    print names

    # Remove behavior from default.
    managerProxy.removeDefaultBehavior(behaviorName)

    names = managerProxy.getDefaultBehaviors()
    print "Default behaviors:"
    print names


if __name__ == "__main__":
    '''    
if (len(sys.argv) < 3):
        print "Usage python albehaviormanager_example.py robotIP behaviorName"
        sys.exit(1)
    '''
    #main(sys.argv[1], sys.argv[2])
    main("127.0.0.1", "behavior_1")
