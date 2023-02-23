import os
import cv2
import torch

# 测试图片位置
path = "./dataset/TAG/test/"
files = os.listdir(path)

device = torch.device("cuda")
# 加载模型，路径需要修改
model = torch.hub.load('D:/PythonProjs/TAG', 'custom', 'D:/PythonProjs/TAG/pretrained/tag200.pt',
                       source='local', force_reload=False)

# 遍历测试图片
for i in range(len(files)):
    img = cv2.imread(path + files[i])
    model = model.to(device)
    results = model(path + files[i])

    # 过滤模型
    xmins = results.pandas().xyxy[0]['xmin']
    ymins = results.pandas().xyxy[0]['ymin']
    xmaxs = results.pandas().xyxy[0]['xmax']
    ymaxs = results.pandas().xyxy[0]['ymax']
    classList = results.pandas().xyxy[0]['class']
    confidences = results.pandas().xyxy[0]['confidence']
    newList = []
    for xmin, ymin, xmax, ymax, classItem, conf in zip(xmins, ymins, xmaxs, ymaxs, classList, confidences):
        if classItem == 0 and conf > 0.5:
            newList.append([int(xmin), int(ymin), int(xmax), int(ymax), conf])

    if len(newList) > 0:
        for listItem in newList:
            cv2.rectangle(img, (listItem[0], listItem[1]), (listItem[2], listItem[3]), (50, 50, 255), 1, lineType=cv2.LINE_AA)
            cv2.putText(img, "conf:" + str(listItem[4]), (listItem[0], listItem[1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (50, 255, 255))
            #cv2.imshow("result", img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            outPath = "./dataset/TAG/results/"
            cv2.imwrite(outPath + files[i], img)
