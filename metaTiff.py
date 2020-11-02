import os
from osgeo import gdal
import numpy as np
# from os.path import join, getsize
def execute(input,output):
     #挑出shp数据路径 
    fileList = os.listdir(input)
    for file in fileList:
        if(file.split('.')[1]== 'tiff' or file.split('.')[1]== 'tif'):
            tiff_file=file
            break
    tiff_data=gdal.Open(input+'/'+tiff_file)
    metaDict={'width':tiff_data.RasterXSize,'height':tiff_data.RasterYSize,'bands':tiff_data.RasterCount,'proj':tiff_data.GetProjection()}
    size = 0
    for root, dirs, files in os.walk(input):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    metaDict['size']=str(size)+'bytes'
    print(metaDict)
    del tiff_data
    return True
if __name__=='__main__':
    i='D:/Projects/processing/input/tiff'
    o='D:/Projects/processing/output/tiff'
    if execute(i,o) is True:
        print('ok')