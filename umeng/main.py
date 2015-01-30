# -*- coding: utf-8 -*-
import commands
import os
from time import sleep
import time
import umeng_config
import edit_build_prop
from shuaji import exec_adb_cmd
import shuaji

#<<<<<<< HEAD
#=======
#def shuaji():
#	print("打开应用")
#	(status, result) = commands.getstatusoutput("adb shell am start -n com.zoneol.lovebirds/.ui.WelcomeActivity")
#	if status == 0 :
#		print("打开应用成功")
#		print("等待 20s")
#		time.sleep(20)
#	else:
#		print("打开应用失败")
#		print(result)
#		return
#	
#	print("清理应用缓存")
#	(status, result) = commands.getstatusoutput("adb shell pm clear com.zoneol.lovebirds")
#	if status == 0 :
#		print("清理应用缓存成功")
#		time.sleep(5)
#	else:
#		print("清理应用缓存失败")
#		return
#	print("执行完成")
#>>>>>>> 815cec01243a6f59ed9d7f951662d2810dfdfcdd
#	
print("开始执行")
count = 0
while count < umeng_config.AMOUNT_OF_DEVICES :
	count += 1
	time_count = 0
	print("更新build.prop")
	edit_build_prop.update_build_prop()

	result = exec_adb_cmd(umeng_config.PUSH_BUILD_PROP_CMD,"将build.prop push到/sdcard/中",10)
	if result != 0:
		exit()
		
	result = exec_adb_cmd(umeng_config.LANUCN_MOUNT_SYSTEM_CMD,"启动mountsystem app，将修改过的build.prop 重定向到/system/build.prop中",10)
	
	exec_adb_cmd(umeng_config.DISCONNECT_ADB_CMD,"disconnect adb",0)

	
	print("正在重启。。。。")
	sleep(40)
	
	print("连接adb")
	connect_time = 0
	
	(status,result) = commands.getstatusoutput(umeng_config.DISCONNECT_ADB_CMD)
	sleep(5)
	(status,result) = commands.getstatusoutput(umeng_config.ADB_KILLSERVER_CMD)
	
	while True:
		(status,result) = commands.getstatusoutput(umeng_config.CONNECT_ADB)
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
	
	for n in range(umeng_config.TIME_FOR_EACH_DEVICE):
		shuaji.shuaji()
		#sleep(10)
	