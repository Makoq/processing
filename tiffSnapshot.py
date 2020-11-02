# plt方式的tiff可视化
import os
import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
#tiff数据的可视化

def execute(input,output):
     #挑出shp数据路径 
    fileList = os.listdir(input)
    for file in fileList:
        if(file.split('.')[1]== 'tiff' or file.split('.')[1]== 'tif'):
            tiff_file=file
            break
    img=Image.open(input+'/'+tiff_file)
    img=np.array(img)# 获得numpy对象, np.ndarray, RGB
    #统一使用plt进行显示，不管是plt还是cv2.imshow,在python中只认numpy.array，但是由于cv2.imread 的图片是BGR，cv2.imshow 时相应的换通道显示 
    plt.imshow(img)
    plt.axis('off')
    plt.savefig(output+'/result.png')
    return True
if __name__=='__main__':
    # i='D:/Projects/testData/tiff'
    # o='D:/Projects/testData/tiff'
    if execute(sys.argv[1],sys.argv[2]) is True:
        print('ok')