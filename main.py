import getpass
import os
import sys
import time

from nuofunction import lianwang

if __name__ == "__main__":
    # 校园网定义
    xiaoyuanurl = ""

    # 校园网账号
    xiaoyuanusername = ""

    # 校园网密码
    xiaoyuanpassword = ""

    # 引入类
    nuo = lianwang()

    # 校园网连接性检测
    if not (nuo.geturl(xiaoyuanurl)):
        print("网络异常或不是校园网，请检查")
        exit(1)

    # 密码验证(防止盗登)
    # sslogin = input("请输入分配给的给予的安全密码：")
    password = getpass.getpass("请输入分配给的给予的安全密码：")
    if password != "nu23o09":
        print("密码错误")
        input("按任意键关闭")
        exit(1)

    # 验证成功后开始检测是否登陆过
    if not (nuo.openurl(xiaoyuanurl)):
        print("浏览器内核调用异常,请检查")
        input("按任意键关闭")
        exit(1)

    print("正在静默登陆中，请稍后....")

    if True in nuo.find("xpath", "/html/body/div/div[1]/div[5]/input"):
        print("检测到登录，开始执行")
        nuo.shell("xpath", "click", "/html/body/div/div[1]/div[5]/input")
    else:
        print("未检测到登录，继续执行")
    # 用户名
    nuo.shell("xpath", "click", "/html/body/div/div[1]/form/input[1]")
    nuo.shell("xpath", "clear", "/html/body/div/div[1]/form/input[1]")
    nuo.shell("xpath", "element", "/html/body/div/div[1]/form/input[1]", xiaoyuanusername)

    # 密码
    nuo.shell("xpath", "click", "/html/body/div/div[1]/form/input[2]")
    nuo.shell("xpath", "clear", "/html/body/div/div[1]/form/input[2]")
    nuo.shell("xpath", "element", "/html/body/div/div[1]/form/input[2]", xiaoyuanpassword)
    nuo.shell("xpath", "click", "/html/body/div/div[1]/form/button")

    # 关闭浏览器内核
    nuo.closeurl()

    print("登录完毕，正在调用系统浏览器用于您检测是否登录成功")
    os.popen("start " + xiaoyuanurl)
    input("按任意键关闭")
