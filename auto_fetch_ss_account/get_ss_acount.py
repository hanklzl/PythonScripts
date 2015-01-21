#coding=utf-8

import requests
import bs4
from bs4 import BeautifulSoup
import json
import os
import subprocess

target_url = "http://www.jslink.org/shadowsocks.php" #�����URL�ܻ�ȡ��һ������룬���������룬��һ�������С����Ϊ���ݾͿ��Թ���һ�����ݰ��������ȡ�˺�
get_params_url = "http://www.jslink.org/about" #���ͻ�ȡ�˺ŵ�URL

params_response = requests.get(get_params_url) #��ȡtarget_url������
if params_response.status_code == 200:
	print("fetch get_params_url success!")
else:
	print("fetch get_params_url failed!")
	exit()
	
soup = BeautifulSoup(params_response.text) #��ʼ������ͨ���������key
key = [a.attrs.get('value') for a in soup.select('div > input')]

if len(key):
	print("get key success " + key[0])
else:
	print("can't get key from " + get_params_url)
	exit()

#����http�����ͷ,cookie���Թ����Ǳ����
header = { 'User-Agent' : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2267.0 Safari/537.36",
#		'Cookie':'PHPSESSID=g8ta6mifu7dskp1it0rms41ro3; Hm_lvt_73001e78a67422e67a4fe526693226aa=1421113618,1421207361; Hm_lpvt_73001e78a67422e67a4fe526693226aa=1421216906',
#		"X-Requested-With":"XMLHttpRequest",
		"Referer":"http://www.jslink.org/about"}


#����http�����data
form_data={'k':key[0],
	't':'0.22469300171360373'}
	
#��������
s = requests.session()
response = s.post(target_url,data = form_data,headers = header)
if response.status_code != 200:
	print("can not get correct response from: ", target_url)
	exit()

#�õ����󷵻ص����ݣ�ת��Ϊjson
new_data = response.json()

#��ss�������ļ�
json_data = open('../gui-config.json')
data = json.load(json_data)
#print(data)

#��������и��˺ŵ����ô��ڣ����޸����е�ֵ������������򴴽�һ�����޸ĺ�д���ļ��������˳�
is_config_exist = 0
for item in data['configs']:
	if item['server'] == "106.186.127.95":
		#print(type(item))
		#print(type(new_data))
		print('config file exist, edit it!')
		item['server_port'] = new_data['server_port']
		item['password'] = new_data['password']
		is_config_exist = 1
		with open('../gui-config.json','w') as outfile:
			outfile.write(unicode(json.dumps(data,ensure_ascii=False)))
		break

if(is_config_exist == 0):
	print("config file not exist, create it!")
	config_lenth = len(data['configs'])
	new_item = dict()
	new_item['server'] = new_data['server']
	new_item['server_port'] = new_data['server_port']
	new_item['local_port'] = 1080
	new_item['password'] = new_data['password']
	new_item['method'] = new_data['method']
	new_item['remarks'] = ""
	data['configs'].append(new_item)
	with open('../gui-config.json','w') as outfile:
			outfile.write(unicode(json.dumps(data,ensure_ascii=False)))
			
print("update complete")
print("starting app")
#os.system("./shadowsocks.exe")
subprocess.Popen(["../shadowsocks.exe"])
exit()
