#coding=utf-8

#ÿ��ˢ���ݵĻ�������
AMOUNT_OF_DEVICES = 50

#ÿ�����ˢ�Ĵ���
TIME_FOR_EACH_DEVICE = 16

#���������б��·��
PATH_DEVICE_NAME = "./DeviceName"

#APK��·��
PATH_APK = "LoveBirds_normao2.apk"

#build.prop��·��
PATH_BUILD_PROP = "build.prop"

#build.prop��"ro.product.model"�����е���ţ���0��ʼ��
DEVICE_NAME_LINE_NUM = 14

#���ʹ��TCP adb���ӵ��ԣ�������������ip
TCP_ADB_ADDR = "192.168.1.106"

#ˢ�����õ�������
#����Ӧ��
LAUCH_APP_CMD = "adb shell am start -n com.zoneol.lovebirds/.ui.WelcomeActivity"

#����Ӧ�û���
CLEAN_APP_CACHE_CMD = "adb shell pm clear com.zoneol.lovebirds"

#��build.prop push�� /sdcard��
PUSH_BUILD_PROP_CMD = "adb push build.prop /sdcard/"

#����mountsystem app
LANUCN_MOUNT_SYSTEM_CMD = "adb shell am start -n com.example.mountsystem/.MainActivity"

#disconnect adb
DISCONNECT_ADB_CMD = "adb disconnect"

#adb killserver
ADB_KILLSERVER_CMD = "adb killserver"

#adb connect
CONNECT_ADB = "adb connect %s" % (TCP_ADB_ADDR,)

