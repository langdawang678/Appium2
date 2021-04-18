# coding=utf-8
from appium import webdriver

# 1.准备参数，那个平台-设备-app-页面
desire_caps = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "emulator-5554",
    "appPackage": "com.philips.powerstrip",
    # "appActivity": "com.philips.powerstrip/com.smart.TuyaSplashActivity",
    "appActivity": "com.smart.TuyaSplashActivity",
    "noReset": True
}

# 启动appium server（桌面程序，ip和端口）windows用管理员运行

# 连接appium server，把启动参数发送
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)

"""
adb查看包名
方法一：adb shell pm list packages
方法二：adb shell dumpsys activity activities （前提条件：手机应用上只启动你要用的APP）
方法三：aapt方法：语句：aapt dump badging 路径和文件名
（1）下载aapt 拽到platform-tools文件夹下（platform-tools已经配置过环境变量了，拽进来就不用再配置了）
（2）如下载汽车之家apk文件（安卓安装包）（可以放在桌面上，写命令时直接拽进来）
"""

'''
appium如何获取到APP的启动activity
https://www.cnblogs.com/handaxing/p/6952491.html
方法一：adb shell monkey -p 包名 -v -v -v 1
方法二： aapt dump bading apk所在路径\apk名字（或者直接把apk拖进命令行）
(package: name=’com.xxx.android.xx’
launchable-activity: name=’com.xxx.android.xx.view.xxxrActivity’)
进入命令行，输入adb logcat|grep START点击待测应用即可

'''


'''
0.0.0.0和127的差别https://blog.csdn.net/chzhli/article/details/95910324
'''
