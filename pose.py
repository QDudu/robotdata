# -*- encoding: UTF-8 -*-

import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):
    # 动作
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    # 可以调用已经定义好的姿势
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # 调用 醒来 动作
    motionProxy.wakeUp()

    # 控制机器人目标姿势为站立初始姿势
    postureProxy.goToPosture("StandInit", 0.5)

    # 调用 休息 动作
    motionProxy.rest()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
