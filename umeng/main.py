# -*- coding: utf-8 -*-
import commands
import os
from time import sleep
import time
import umeng_config
import edit_build_prop

def shuaji():
#	(status, result) = commands.getstatusoutput("adb install -r LoveBirds_normao2.apk")
#	if status == 0:
#		print("��װ�ɹ�")
#	else:
#		print("��װʧ��")
#		print(result)
#		return
	print("��Ӧ��")
	(status, result) = commands.getstatusoutput("adb shell am start -n com.zoneol.lovebirds/.ui.WelcomeActivity")
	if status == 0 :
		print("��Ӧ�óɹ�")
		print("�ȴ� 20s")
		time.sleep(20)
	else:
		print("��Ӧ��ʧ��")
		print(result)
		return
	
	print("����Ӧ�û���")
	(status, result) = commands.getstatusoutput("adb shell pm clear com.zoneol.lovebirds")
	if status == 0 :
		print("����Ӧ�û���ɹ�")
		time.sleep(5)
	else:
		print("����Ӧ�û���ʧ��")
		return
	print("ִ�����")
	
print("��ʼִ��")
count = 0
while count < umeng_config.AMOUNT_OF_DEVICES :
	count += 1
	time_count = 0
	edit_build_prop.update_build_prop()
	print("��build.prop push��/sdcard/��")
	
	sleep(10)
	
	(status, result) = commands.getstatusoutput("adb push build.prop /sdcard/")
	sleep(10)
	
	(status, result) = commands.getstatusoutput("adb shell am start -n com.example.mountsystem/.MainActivity")
	if status == 0:
		print("mount /system and modify build.prop success")
	else:
		print("mount /system and modify build.prop failed")
		exit()
	(status, result) = commands.getstatusoutput("adb disconnect")	
	sleep(20)
	
	print("����������������")
	sleep(40)
	
	print("����adb")
	connect_time = 0
	
	(status,result) = commands.getstatusoutput("adb kill-server")
	
	while True:
		(status,result) = commands.getstatusoutput("adb connect 192.168.1.101")
		if status == 0:
			connect_time += 1;
			print("����adb�ɹ�")
			sleep(5)
			if(connect_time == 3):
				connect_time = 0
				break
		else:
			print("����adbʧ�ܣ�����")
			continue
	
	while time_count < umeng_config.TIME_FOR_EACH_DEVICE :
		time_count = time_count + 1
		shuaji()
		sleep(30)
	