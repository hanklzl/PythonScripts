# -*- coding: utf-8 -*-
import commands
import os
from time import sleep
import time
import umeng_config
import edit_build_prop
from shuaji import exec_adb_cmd
import shuaji

	
print("��ʼִ��")
count = 0
while count < umeng_config.AMOUNT_OF_DEVICES :
	count += 1
	time_count = 0
	print("����build.prop")
	edit_build_prop.update_build_prop()

	result = exec_adb_cmd(umeng_config.PUSH_BUILD_PROP_CMD,"��build.prop push��/sdcard/��",10)
	if result != 0:
		exit()
		
	result = exec_adb_cmd(umeng_config.LANUCN_MOUNT_SYSTEM_CMD,"����mountsystem app�����޸Ĺ���build.prop �ض���/system/build.prop��",10)
	if result != 0:
		exit()
	
	exec_adb_cmd(umeng_config.DISCONNECT_ADB_CMD,"disconnect adb",0)

	
	print("����������������")
	sleep(40)
	
	print("����adb")
	connect_time = 0
	
	(status,result) = commands.getstatusoutput(umeng_config.DISCONNECT_ADB_CMD)
	sleep(5)
	(status,result) = commands.getstatusoutput(umeng_config.ADB_KILLSERVER_CMD)
	
	while True:
		(status,result) = commands.getstatusoutput(umeng_config.CONNECT_ADB)
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
	
#	while time_count < umeng_config.TIME_FOR_EACH_DEVICE :
#		time_count = time_count + 1
	for n in range(umeng_config.TIME_FOR_EACH_DEVICE):
		shuaji.shuaji()
		sleep(10)
	