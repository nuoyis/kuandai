import getpass
import os
import sys
import time
import ctypes
from time import sleep
from subprocess import run, PIPE

from nuofunction import lianwang

# 校园网定义
xiaoyuanurl = "http://172.17.1.2"

# 校园网账号
xiaoyuanusername = "230303015"

# 校园网密码
xiaoyuanpassword = "182210"


def admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def login():
    # 验证成功后开始检测是否登陆过
    if not (nuo.openurl(xiaoyuanurl)):
        print("浏览器内核调用异常,请检查")
        input("按任意键关闭")
        exit(1)

    print("正在静默登陆中，请稍后....")

    if True in nuo.find("xpath", "/html/body/div/div[1]/div[3]/div[5]/input"):
        print("检测到登录，开始执行")
        nuo.shell("xpath", "click", "/html/body/div/div[1]/div[3]/div[5]/input")
    else:
        print("未检测到登录，继续执行")
    sleep(10)
    # 用户名
    nuo.shell("xpath", "click", "/html/body/div/div[3]/form/input[1]")
    nuo.shell("xpath", "clear", "/html/body/div/div[3]/form/input[1]")
    nuo.shell("xpath", "element", "/html/body/div/div/div[3]/form/input[1]", xiaoyuanusername)

    # 密码
    nuo.shell("xpath", "click", "/html/body/div/div[3]/form/input[2]")
    nuo.shell("xpath", "clear", "/html/body/div/div[3]/form/input[2]")
    nuo.shell("xpath", "element", "/html/body/div/div/div[3]/form/input[2]", xiaoyuanpassword)
    nuo.shell("xpath", "click", "/html/body/div/div/div[3]/form/button")

    # 关闭浏览器内核
    nuo.closeurl()


if __name__ == "__main__":
    cnt = 1
    while True:
        r = run('ping www.baidu.com',
                stdout=PIPE,
                stderr=PIPE,
                stdin=PIPE,
                shell=True)
        if r.returncode:
            print('登录状态：异常 登录次数:{}次'.format(cnt))
            # 引入类
            nuo = lianwang()

            # 校园网连接性检测
            if not (nuo.geturl(xiaoyuanurl)):
                print("网络异常或不是校园网，请检查")
                exit(1)
            login()
            print('登录请求:成功')
            print('登录状态:正常')
            cnt += 1
        else:
            print('登录状态:正常')
        sleep(60 * 30)  # 每半个小时检查一次

    # 密码验证(防止盗登)
    # sslogin = input("请输入分配给的给予的安全密码：")
    # password = getpass.getpass("请输入分配给的给予的安全密码：")
    # if password != "nu23o09":
    #     print("密码错误")
    #     input("按任意键关闭")
    #     exit(1)
