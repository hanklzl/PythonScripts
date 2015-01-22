#coding=utf-8
import os
import umeng_config
import random
import linecache
import string

def __get_random_device_name():
	count = len(linecache.getlines(umeng_config.PATH_DEVICE_NAME))
	line_num = random.randint(0,count - 1)
	linecache.clearcache()
	return linecache.getline(umeng_config.PATH_DEVICE_NAME,line_num)
	
def update_build_prop():
	new_device_name = __get_random_device_name()
	print("new device name: " + new_device_name)
	file_build_prop = open(umeng_config.PATH_BUILD_PROP).readlines()
	if string.find(file_build_prop[umeng_config.DEVICE_NAME_LINE_NUM],"ro.product.model") != -1:
		print("build.prop ro.product.model found :" + file_build_prop[umeng_config.DEVICE_NAME_LINE_NUM])
		file_build_prop[umeng_config.DEVICE_NAME_LINE_NUM] = new_device_name
		f = open(umeng_config.PATH_BUILD_PROP,'w+')
		f.writelines(file_build_prop)
		return 1
	else:
		print("could not find")
		exit()
	
	
