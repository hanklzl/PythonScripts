# -*- coding: utf-8 -*-
import umeng_config
import commands
import time

def shuaji():
	#打开应用
	result = exec_adb_cmd(umeng_config.LAUCH_APP_CMD,"launch app",10)
	if result != 0:
		return
		
	#清理缓存
	result = exec_adb_cmd(umeng_config.CLEAN_APP_CACHE_CMD,"clear app cache",5)
	if result != 0:
		return
	print("执行完成")
	
	
def exec_adb_cmd(command,cmd_str,sleep_time = 10):
	print(cmd_str)
	(status,result) = commands.getstatusoutput(command)
	if status == 0:
		print(cmd_str + " success")
		print("sleep %s sec" % (sleep_time,))
		time.sleep(sleep_time)
	else:
		print(cmd_str + " failed")
	
	return status
	
if __name__ == "__main__":
		shuaji()
		n = n + 1