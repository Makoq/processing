import sys
import os
import shapefile  #导入模块
#按城市名提取对应城市的shp数据，即数据抽取
def execute(input,output,cityName):
    fileList = os.listdir(input)
    #挑出shp数据 
    for file in fileList:
        if(file.split('.')[1]== 'shp'):
            shp_file=file
            break
    sf = shapefile.Reader(input+'/'+shp_file) #苹姐shp路径，读入shp文件    
    w = shapefile.Writer(output+"/re")
    w.fields = sf.fields[1:] 
    for it in sf.iterShapeRecords():
        if(cityName in it.record[0:]):
            w.record(*it.record)
            w.shape(it.shape)
            return True
    w.close()
if __name__ == "__main__":
    if execute(sys.argv[1],sys.argv[2],sys.argv[3]) is True:
        print("ok")
      
