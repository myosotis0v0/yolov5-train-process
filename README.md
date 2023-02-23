# 配置anaconda虚拟环境,安装pytorch及cuda

参考https://www.bilibili.com/video/BV1hE411t7RN/?spm_id_from=333.999.0.0&vd_source=4fec2a7ab50466980de6deb914433514

注意创建的python版本>=3.7，torch版本最新即可

根据视频配置完成并新建虚拟环境后，打开anaconda prompt依次输入如下指令检测配置是否成功（yolov5为创建的环境名）:
![image](https://github.com/myosotis0v0/yolov5-train-process/blob/main/img/1.png)

# 下载yolov5源码并调试

参考https://zhuanlan.zhihu.com/p/502395993

yolov5源码地址：https://github.com/ultralytics/yolov5

通过git pull或download zip下载后，在anaconda prompt中切换至先前创建的虚拟环境并cd至yolov5项目目录

测试指令：python detect.py --source data/images/bus.jpg --weights pretrained/yolov5s.pt

此处yolov5s.pt为预训练权重，需要在yolov5的github页面readme中点击下载：
