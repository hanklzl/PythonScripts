#coding=utf-8

#每次刷数据的机型数量
AMOUNT_OF_DEVICES = 50

#每款机型刷的次数
TIME_FOR_EACH_DEVICE = 16

#机型名称列表的路径
PATH_DEVICE_NAME = "./DeviceName"

#APK的路径
PATH_APK = "LoveBirds_normao2.apk"

#build.prop的路径
PATH_BUILD_PROP = "build.prop"

#build.prop中"ro.product.model"所在行的序号，从0开始算
DEVICE_NAME_LINE_NUM = 14

#如果使用TCP adb连接电脑，请在这里配置ip
TCP_ADB_ADDR = "192.168.1.106"

#刷数据用到的命令
#启动应用
LAUCH_APP_CMD = "adb shell am start -n com.zoneol.lovebirds/.ui.WelcomeActivity"

#清理应用缓存
CLEAN_APP_CACHE_CMD = "adb shell pm clear com.zoneol.lovebirds"

#将build.prop push到 /sdcard中
PUSH_BUILD_PROP_CMD = "adb push build.prop /sdcard/"

#启动mountsystem app
LANUCN_MOUNT_SYSTEM_CMD = "adb shell am start -n com.example.mountsystem/.MainActivity"

#disconnect adb
DISCONNECT_ADB_CMD = "adb disconnect"

#adb killserver
ADB_KILLSERVER_CMD = "adb killserver"

#adb connect
CONNECT_ADB = "adb connect %s" % (TCP_ADB_ADDR,)

