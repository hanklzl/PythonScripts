#coding=utf-8
#每次刷数据的机型数量
AMOUNT_OF_DEVICES = 20

#每款机型刷的次数
TIME_FOR_EACH_DEVICE = 10

#机型名称列表的路径
PATH_DEVICE_NAME = "./DeviceName"

#APK的路径
PATH_APK = "LoveBirds_normao2.apk"

#build.prop的路径
PATH_BUILD_PROP = "build.prop"

#build.prop中"ro.product.model"所在行的序号，从0开始算
DEVICE_NAME_LINE_NUM = 15