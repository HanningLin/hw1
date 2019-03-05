# 数字图像处理HW1
- 林汉宁  自动化52 2150504042
- 提交日期：2019-03-05
## 摘要
本次作业使用python面向对象方式编程，使用了opencv库。
针对问题一, “Bmp图像格式简介”。使用python opencv imread函数读取bmp格式图像数据进行分析。
针对问题二，依然使用opencv python imread读取图像数据，通过运算改变图像灰度级。
针对问题三，使用opencv 与numpy库计算图像均值方差
针对问题四，使用opencv resize函数差值。
针对问题五，根据定义使用opencv 与numpy库编写函数实现功能。
## 技术讨论
### 1. Bmp图像格式简介
#### 源代码
	def show(self):
	   print("data is {}".format(self.img))
       cv.imshow("7.bmp",self.img)
       cv.waitKey(30)
        
BMP（全称Bitmap）是Windows操作系统中的标准图像文件格式，可以分成两类：设备有向量相关位图（DDB）和设备无向量相关位图（DIB），使用非常广。它采用位映射存储格式，除了图像深度可选以外，不采用其他任何压缩，因此，BMP文件所占用的空间很大。BMP文件的图像深度可选lbit、4bit、8bit及24bit。BMP文件存储数据时，图像的扫描方式是按从左到右、从下到上的顺序。由于BMP文件格式是Windows环境中交换与图有关的数据的一种标准，因此在Windows环境中运行的图形图像软件都支持BMP图像格式。
BMP图像一个位数组，由红、绿、蓝（RGB）三个值代表一个像素。如果是灰度图则三位相同。如下图python opencv imread 部分数据所示：![bmp数据](http://ww1.sinaimg.cn/large/006tquCMly1g0s6wxahu1j309p0ah3yj.jpg)
### 2. 把lena 512*512图像灰度级逐级递减8-1显示
#### 源代码
	def cvtGrayLevel(self,level):
        #level is bpp
        level=int(level)
        # print("#level is {}".format(level))
        new_img=self.img
        if level<9 and level>0:
            scale=int(math.pow(2,8-level))#!!!
            # index=int(256/(gray_level-1))
            # gray_num=range(0,gray_level*index,index)
            # for temp in range(gray_level):
            #     print("index is {}".format(gray_num[temp]))
            dimensions=new_img.shape
            height = dimensions[0]
            width = dimensions[1]
            channels = dimensions[2]
            # print("height:{},width:{},channels:{}".format(height,width,channels))
            for i in range(height):
                for j in range(width):
                    temp=self.img[i][j][0]#digit
                    temp=int(temp/scale)*scale
                    new_img[i][j][0]=temp
                    new_img[i][j][1]=temp
                    new_img[i][j][2]=temp
            cv.imwrite('lena{}bpp.png'.format(level),new_img)
            cv.imshow("lena{}bpp".format(level),new_img)
            k = cv.waitKey(0) & 0xFF
            if k == 27:         # 按下ESC退出
                cv.destroyAllWindows()
#### 代码思路
首先使用opencv库函数imread读取数据，再根据相应灰度级修改对应像素灰度值。
#### 结果
lena8bpp：
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s7fdjhtij30e80e813c.jpg)
lena7bpp:
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s7g5p7xsj30e80e8ai6.jpg)
lena6bpp:
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s7gfzx77j30e80e8gri.jpg)
lena5bpp:
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s7gpgi19j30e80e8jvg.jpg)
lena4bpp:
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s7hquzihj30e80e8acp.jpg)
lena3bpp:
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s7i0pnauj30e80e8abo.jpg)
lena2bpp:
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s7i8m60zj30e80e80tk.jpg)
lena1bpp:
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s7ifq4ylj30e80e8glr.jpg)

### 3.计算lena图像的均值方差
#### 源代码
	def caculateMeanVariance(self):
        (mean , stddv) = cv.meanStdDev(self.img)
        print("mean:{},stdDev:{}".format(mean,stddv))
#### 代码思路
使用opencv自带meanStdDev函数可计算均值与方差
#### 最终结果
均值|方差
---|---
99.09011078|52.73530213
### 4.把lena图像用近邻、双线性和双三次插值法zoom到2048*2048
#### 源代码
	def resize(self):
        new_img_N=cv.resize(self.img,(2048,2048),interpolation=cv.INTER_NEAREST)
        new_img_B=cv.resize(self.img,(2048,2048),interpolation=cv.INTER_LINEAR)
        new_img_C=cv.resize(self.img,(2048,2048),interpolation=cv.INTER_CUBIC)
        cv.imwrite('1-3_ZOOM_Nearest.png',new_img_N)
        cv.imwrite('1-3_ZOOM_Bilinear.png',new_img_B)
        cv.imwrite('1-3_ZOOM_Cubic.png',new_img_C)
#### 代码思路
使用opencv库函数resize使用不同方法进行差值
#### 结果展示
最近邻插值：
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s7tsmqd2j31kw1kwe82.jpg)
双线性插值：
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s7v3xb91j31kw1kwkjm.jpg)
双三次插值：
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s7znh781j31kw1kw1kz.jpg)
### 5、把lena和elain图像分别进行水平shear（参数可设置为1.5，或者自行选择）和旋转30度，并采用用近邻、双线性和双三次插值法zoom到2048*2048；
#### 源代码
	def shearZoom(self,parameter):
        a = parameter#sv shear parameter =tan(a)
        dimensions=self.img.shape
        height = dimensions[0]
        width = dimensions[1]
        channels = dimensions[2]
        W=width
        H=int(height+width*a)
        img_shear=numpy.zeros((W,H,channels), numpy.uint8)
        for i in range(height):
            for j in range(width):
                y = int(i*a+j)
                img_shear[i,y] = self.img[i,j]
        # cv.imwrite('lena shear.png',new_img)
        # cv.imshow("after shear",img_shear)
        # k = cv.waitKey(0) & 0xFF
        # if k == 27:         # 按下ESC退出
        #     cv.destroyAllWindows()
        ####################ZOOM######################
        shear_zoom_img_N=cv.resize(img_shear,(2048,2048),interpolation=cv.INTER_NEAREST)
        shear_zoom_img_B=cv.resize(img_shear,(2048,2048),interpolation=cv.INTER_LINEAR)
        shear_zoom_img_C=cv.resize(img_shear,(2048,2048),interpolation=cv.INTER_CUBIC)
        cv.imwrite('1-4_SHEAR_ZOOM_Nearest.png',shear_zoom_img_N)
        cv.imwrite('1-4_SHEAR_ZOOM_Bilinear.png',shear_zoom_img_B)
        cv.imwrite('1-4_SHEAR_ZOOM_Cubic.png',shear_zoom_img_C)


    def RotateZoom(self,parameter):
        #parameter is an angle e.p:30=pi/6
        ###########ROTATION##########
        angle=parameter
        dimensions=self.img.shape
        height = dimensions[0]
        width = dimensions[1]
        channels = dimensions[2]
        cosa=math.cos(angle*math.pi/180.0)
        sina=math.sin(angle*math.pi/180.0)
        W=round(width*cosa+height*sina)
        H=round(height*cosa+width*sina)
        img_rotate=numpy.zeros((W,H,channels), numpy.uint8)
        for i in range(height):
            for j in range(width):
                x=int(i*cosa-j*sina)
                y=int(i*sina+j*cosa)
                img_rotate[x,y] = self.img[i,j]
        # # cv.imwrite('elain_rotate.png',new_img)
        new_img_rotate=numpy.zeros((W,H,channels), numpy.uint8)
        new_img_rotate[0:int(width*sina),:]=img_rotate[int(height*cosa):H-1,:]
        new_img_rotate[int(width*sina):H,:]=img_rotate[0:round(height*cosa)+1,:]
        # img_rotate=cv.getRotationMatrix2D((int(width/2),int(height/2)), angle, 1.0)
        # cv.imshow("after shear",new_img_rotate)
        # k = cv.waitKey(0) & 0xFF
        # if k == 27:         # 按下ESC退出
        #     cv.destroyAllWindows()
        ####################ZOOM######################
        rotate_zoom_img_N=cv.resize(new_img_rotate,(2048,2048),interpolation=cv.INTER_NEAREST)
        rotate_zoom_img_B=cv.resize(new_img_rotate,(2048,2048),interpolation=cv.INTER_LINEAR)
        rotate_zoom_img_C=cv.resize(new_img_rotate,(2048,2048),interpolation=cv.INTER_CUBIC)
        cv.imwrite('1-4_ROTATE_ZOOM_Nearest.png',rotate_zoom_img_N)
        cv.imwrite('1-4_ROTATE_ZOOM_Bilinear.png',rotate_zoom_img_B)
        cv.imwrite('1-4_ROTATE_ZOOM_Cubic.png',rotate_zoom_img_C)
#### 代码思路
使用numpy与math python库进行矩阵运算分别对图像进行错切与旋转操作再使用opencv库resize函数对图像进行缩放。
#### 结果展示
- lena
	- 邻近
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s800q10tj31kw1kw1ky.jpg)
	- 双线性
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s838zhvdj31kw1kwu0x.jpg)
	- 双三次
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s85nvt16j31kw1kw1ky.jpg)
- elain
	- 邻近
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s807aq5kj31kw1kw7wi.jpg)
	- 双线性
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s83e05czj31kw1kwb2b.jpg)
	- 双三次
![](http://ww1.sinaimg.cn/large/006tquCMly1g0s85z6w9rj31kw1kwu10.jpg)

### 参考
[OpenCV-Python Tutorials](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)
[Python 基础教程](http://www.runoob.com/python/python-tutorial.html)


