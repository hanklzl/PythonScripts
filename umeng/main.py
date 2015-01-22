# -*- coding: utf-8 -*-
import commands
import os
from time import sleep
import time
import umeng_config
import edit_build_prop

def shuaji():
	print("打开应用")
	(status, result) = commands.getstatusoutput("adb shell am start -n com.zoneol.lovebirds/.ui.WelcomeActivity")
	if status == 0 :
		print("打开应用成功")
		print("等待 20s")
		time.sleep(20)
	else:
		print("打开应用失败")
		print(result)
		return
	
	print("清理应用缓存")
	(status, result) = commands.getstatusoutput("adb shell pm clear com.zoneol.lovebirds")
	if status == 0 :
		print("清理应用缓存成功")
		time.sleep(5)
	else:
		print("清理应用缓存失败")
		return
	print("执行完成")
	
print("开始执行")
count = 0
while count < umeng_config.AMOUNT_OF_DEVICES :
	count += 1
	time_count = 0
	edit_build_prop.update_build_prop()
	print("将build.prop push到/sdcard/中")
	
	sleep(10)
	
	(status, result) = commands.getstatusoutput("adb push build.prop /sdcard/")
	sleep(10)
	
	print("启动mountsystem app，将修改过的build.prop 重定向到/system/build.prop中")
	(status, result) = commands.getstatusoutput("adb shell am start -n com.example.mountsystem/.MainActivity")
	if status == 0:
		print("mount /system and modify build.prop success")
	else:
		print("mount /system and modify build.prop failed")
		exit()
	(status, result) = commands.getstatusoutput("adb disconnect")	
	sleep(20)
	
	print("正在重启。。。。")
	sleep(40)
	
	print("连接adb")
	connect_time = 0
	
	kill_time = 0
	while(kill_time < 3):
		(status,result) = commands.getstatusoutput("adb disconnect")
		(status,result) = commands.getstatusoutput("adb kill-server")
		kill_time += 1
	
	while True:
		(status,result) = commands.getstatusoutput("adb connect 192.168.1.101")
		if status == 0:
			connect_time += 1;
			print("连接adb成功")
			sleep(5)
			if(connect_time == 3):
				connect_time = 0
				break
		else:
			print("连接adb失败，重试")
			continue
	
	while time_count < umeng_config.TIME_FOR_EACH_DEVICE :
		time_count = time_count + 1
		shuaji()
		sleep(30)
	