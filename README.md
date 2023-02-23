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
![image](https://github.com/myosotis0v0/yolov5-train-process/blob/main/img/2.png)

下载完成后置于yolov5项目文件夹中新建的pretrained文件夹并执行测试指令，可在runs\detect\exp文件夹中看到标注了检测结果的bus.jpg：
![image](https://github.com/myosotis0v0/yolov5-train-process/blob/main/img/bus.jpg)

# 制作并训练数据集
参考https://www.bilibili.com/video/BV1f94y1R7a4/?spm_id_from=333.999.0.0

参考https://zhuanlan.zhihu.com/p/502395993

yolov5数据集文件结构：train文件夹和val文件夹分别为训练集和验证集，理论上训练集合理数量为验证集的5倍左右，train和val文件夹下分别都有两个images和labels文件夹，存储图片及对应的标签（txt文件）。训练时，yolov5会在images文件夹的父目录下寻找labels文件夹，因此images和labels文件夹需置于同一目录

在虚拟环境下使用pip install labelimg命令安装labelimg软件，并输入labelimg命令启动后，即可进行打标

数据集格式选择yolo，open dir选择train或val下的images文件夹，save dir选择对应的labels文件夹，按w键开始框选，最终需要完成train\images和val\images所有图片的打标

制作ymal文件，用途为说明train和val路径以及标签数量，示例：
![image](https://github.com/myosotis0v0/yolov5-train-process/blob/main/img/3.png)

开始训练，cd至yolov5项目目录，指令：python train.py --batch-size 1 --epochs 100 --data .\dataset\TAG\data.yaml --weights .\pretrained\yolov5s.pt

其中yaml文件和.pt预训练权重文件路径根据实际情况选择，batch-size取决于gpu显存大小或内存大小（用cpu训练时），epochs 100代表该次训练100轮

训练结果保存于runs\train\expxxx文件夹中，其中权重文件可以作为下次训练的预训练权重使用

# 验证训练结果
参考test_model.py


