# -*- coding: utf-8 -*-
import commands
import os
import time
ext_count = 0
count = 0
raw_input_str = "���������:"
ext_count = int(raw_input(raw_input_str + " \n"))

#print("��ʼִ��")
while count < ext_count :
	count += 1
	print("���ڰ�װ�����")
	(status, result) = commands.getstatusoutput("adb install -r LoveBirds_normao2.apk")
	if status == 0:
		print("��װ�ɹ�")
	else:
		print("��װʧ��")
		print(result)
		continue
	print("��Ӧ��")
	(status, result) = commands.getstatusoutput("adb shell am start -n com.zoneol.lovebirds/.ui.WelcomeActivity")
	if status == 0 :
		print("��Ӧ�óɹ�")
		print("�ȴ� 20s")
		time.sleep(20)
	else:
		print("��Ӧ��ʧ��")
		print(result)
		continue
	
	print("����Ӧ�û���")
	(status, result) = commands.getstatusoutput("adb shell pm clear com.zoneol.lovebirds")
	if status == 0 :
		print("����Ӧ�û���ɹ�")
		time.sleep(10)
	else:
		print("����Ӧ�û���ʧ��")
		continue
	print("��" , count , "ִ�����")
