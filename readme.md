### introduction：

​	本项目是笔者假期闲着无聊做着玩的一个花朵识别系统。

· 可识别五种植物，准确率大于85

· 通过PyQt5可视化

· 爬虫百度图片、百度百科、植物数据中心等图片和文本数据

· 词云显示词频

· 图品轮播展示功能



### explain：

文件夹：
face_trainer：存放人脸登录数据训练结果
Facedata：存放录入的人脸数据
flower_data：植物识别用到的训练数据

文件：
AlexNet.pth：植物识别训练结果
bdbk.py：百度百科爬虫
ciyun.py：生成词云图
class_indices.json：植物代号
data_get.py：爬取花朵图片数据
face_recognize.py：人脸识别
faces_input_frame.py：人脸数据录入
faces_register.py：账号密码注册
haarcascade_frontalface_default.xml：调用摄像头所需文件
login.py：初始登录界面
login2.py：登录界面
model.py：植物识别网络建模
papic.py：百度图片爬虫
papic2.py：爬取www.plantplus.cn植物科学数据中心对应花朵的二维码图片
predict.py：植物识别预测
split_data.py：对数据操作函数（已不需要运行）
train.log：训练过程记录
train.py：植物识别训练
user_names.txt：登录账号密码
user_names_admin.txt：人脸登录账号
v1.py：植物识别界面
v2.py：目前主函数