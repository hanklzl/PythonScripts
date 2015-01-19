# -*- coding: utf-8 -*-
import commands
import os
import time
ext_count = 0
count = 0
raw_input_str = "请输入次数:"
ext_count = int(raw_input(raw_input_str + " \n"))

#print("开始执行")
while count < ext_count :
	count += 1
	print("正在安装软件包")
	(status, result) = commands.getstatusoutput("adb install -r LoveBirds_normao2.apk")
	if status == 0:
		print("安装成功")
	else:
		print("安装失败")
		print(result)
		continue
	print("打开应用")
	(status, result) = commands.getstatusoutput("adb shell am start -n com.zoneol.lovebirds/.ui.WelcomeActivity")
	if status == 0 :
		print("打开应用成功")
		print("等待 20s")
		time.sleep(20)
	else:
		print("打开应用失败")
		print(result)
		continue
	
	print("清理应用缓存")
	(status, result) = commands.getstatusoutput("adb shell pm clear com.zoneol.lovebirds")
	if status == 0 :
		print("清理应用缓存成功")
		time.sleep(10)
	else:
		print("清理应用缓存失败")
		continue
	print("第" , count , "执行完成")
