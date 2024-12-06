# Duo S 蓝牙初始化操作说明
hciattach -s 1500000 /dev/ttyS4 any 1500000 flow nosleep # 启动蓝牙服务
hciconfig hci0 up
hcitool scan

# 第三方蓝牙协议栈适配说明
替换 Makefile 文件到 `mynewt-nimble/porting/npl/linux/test/Makefile`