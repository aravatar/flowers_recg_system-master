# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:44:25 2022

@author: gldz
"""

# -*- coding: utf-8 -*-
#face_recognize.py程序
def Collect_faces():
    import cv2
    import os
    # 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
 
    cap = cv2.VideoCapture(0)
 
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
    fl = open('user_names_admin.txt', 'r+')
    pre_name=fl.read()
    name = pre_name.split(',')
    face_id=len(name) - 2#去掉逗号及以零开始的序号，表示某人的一些列照片
    fl.close()
    #face_id = input('\n enter user id:')  #输入序号，表示某人的一些列照片
 
    print('\n Initializing face capture. Look at the camera and wait ...')
 
    count = 0
 
    while True:
 
        # 从摄像头读取图片
 
        sucess, img = cap.read()
 
        # 转为灰度图片
 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
        # 检测人脸
 
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
 
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + w), (255, 0, 0))
            count += 1
 
            # 保存图像,从原始照片中截取人脸尺寸
            cv2.imwrite("Facedata/User." +str(face_id) + '.' + str(count) + '.jpg', gray[y: y + h, x: x + w])
 
            cv2.imshow('image', img)
 
        # 保持画面的持续。
 
        k = cv2.waitKey(1)
 
        if k == 27:  # 通过esc键退出摄像
            break
 
        elif count >=150:  # 得到150个样本后退出摄像
            break
 
    # 关闭摄像头
    cap.release()
    cv2.destroyAllWindows()
 
def Training_faces():
    import numpy as np
    from PIL import Image
    import os
    import cv2
    # 人脸数据路径
    path = 'Facedata'
 
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
 
    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]  
        faceSamples = []
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')  
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x: x + w])
                ids.append(id)
        return faceSamples, ids
 
    print('Training faces. It will take a few seconds. Wait ...')
    faces, ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))
 
    recognizer.write(r'face_trainer\trainer.yml')
    print("{0} faces trained. Exiting Program".format(len(np.unique(ids))))
 
def recognize_face():
    #识别时间10秒；如果置信度大于60%，则识别成功并退出界面；否则至10秒后识别失败并退出
    import cv2
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('face_trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX
    idnum =None #初始化识别序号
    fl = open('user_names_admin.txt', 'r+')
    pre_name = fl.read()
    names = pre_name.split(',')
 
    cam = cv2.VideoCapture(0)
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    time=0
    while True:
        result = "unknown"   #初始化识别失败
        time+=1
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH))
        )
        face_num=None  #初始化人脸序号
 
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            idnum, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            if confidence>60: #60%的识别置信度
                face_num=idnum
                result= names[idnum]
                confidence = "{0}%".format(round(100 - confidence))
                cam.release()
                cv2.destroyAllWindows()  #退出摄像头
                return result
            else:
                confidence = "{0}%".format(round(100 - confidence))
            cv2.putText(img, str(face_num), (x + 5, y - 5), font, 1, (0, 0, 255), 1)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (0, 0, 0), 1)
        cv2.imshow('camera', img)#弹出摄像头与否
        k = cv2.waitKey(1)
        if k == 27:
            break
        elif time>100:  # 大约10秒识别时间
            break
    cam.release()
    cv2.destroyAllWindows()
    return result   #返回识别结果：人名或“unknown”