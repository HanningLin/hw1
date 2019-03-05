import cv2 as cv
import math
import numpy

class Pic:
    def __init__(self, name, path):
         self.name=name
         self.path=path
         self.img=cv.imread(path)
    def show(self):
        print("data is {}".format(self.img))
        cv.imshow("7.bmp",self.img)
        cv.waitKey(30)
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
    def caculateMeanVariance(self):
        (mean , stddv) = cv.meanStdDev(self.img)
        print("mean:{},stdDev:{}".format(mean,stddv))
    def resize(self):
        new_img_N=cv.resize(self.img,(2048,2048),interpolation=cv.INTER_NEAREST)
        new_img_B=cv.resize(self.img,(2048,2048),interpolation=cv.INTER_LINEAR)
        new_img_C=cv.resize(self.img,(2048,2048),interpolation=cv.INTER_CUBIC)
        cv.imwrite('1-3_ZOOM_Nearest.png',new_img_N)
        cv.imwrite('1-3_ZOOM_Bilinear.png',new_img_B)
        cv.imwrite('1-3_ZOOM_Cubic.png',new_img_C)
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



print("#ANS:1-1\n")
img7=Pic("img7","/home/hanninglin/Documents/CV/PROJECT/CV-class-Project1/hw1/7.bmp")
print("name:{}".format(img7.name))
img7.show()
# print("#ANS:1-2\n")
lena=Pic("lena","/home/hanninglin/Documents/CV/PROJECT/CV-class-Project1/hw1/lena.jpg")
# lena.cvtGrayLevel(8)
# lena.cvtGrayLevel(7)
# lena.cvtGrayLevel(6)
# lena.cvtGrayLevel(5)
# lena.cvtGrayLevel(4)
# lena.cvtGrayLevel(3)
# lena.cvtGrayLevel(2)
# lena.cvtGrayLevel(1)
print("#ANS:1-3\n")
lena.caculateMeanVariance()
print("#ANS:1-4\n")
lena.resize()
print("#ANS:1-4\n")
elain=Pic("elain","/home/hanninglin/Documents/CV/PROJECT/CV-class-Project1/hw1/elain.jpg")
# lena.shearZoom(1.5)
elain.RotateZoom(30)